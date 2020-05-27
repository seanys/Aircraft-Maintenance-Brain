package com.luence.util;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Date;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.DateTools;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.store.SimpleFSDirectory;
import org.apache.lucene.util.Version;
import org.apache.pdfbox.pdfparser.PDFParser;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.util.PDFTextStripper;
import org.apache.poi.hwpf.extractor.WordExtractor;
import org.apache.poi.xwpf.extractor.XWPFWordExtractor;
import org.apache.poi.xwpf.usermodel.XWPFDocument;

public class LuceneCreateIndex {

	/**
	 * @param args
	 * @throws IOException
	 */

	public static void creatIndex(String dataFilePath, String indexFilePath) throws IOException {
		// 保存word文件的路�?
		String dataDirectory = dataFilePath;
		// 保存Lucene索引文件的路�?
		String indexDirectory = indexFilePath;
		File dataDir = new File(dataDirectory);
		File indexDir = new File(indexDirectory);
		// 创建Directory对象 ，也就是分词器对�?
		Directory directory = new SimpleFSDirectory(new File(indexDirectory));
		// 创建�?个简单的分词�?,可以对数据进行分�?
		Analyzer analyzer = new StandardAnalyzer(Version.LUCENE_43);

		// 创建索引实例
		// �?1个参数是Directory,
		// �?2个是分词�?,
		// �?3个表示是否是创建, true代表覆盖原先数据, 如果为false为在此基�?上面修改,
		// �?4个MaxFieldLength表示对每个Field限制建立分词索引的最大数目，
		// 如果是MaxFieldLength.UNLIMITED，表示长度没有限�?;
		// 如果是MaxFieldLength.LIMITED则表示有限制，可以�?�过IndexWriter对象的setMaxFieldLength（int
		// n）进行指�?

		IndexWriterConfig iwc = new IndexWriterConfig(Version.LUCENE_43, analyzer);
		IndexWriter indexWriter = new IndexWriter(FSDirectory.open(indexDir), iwc);
		// 获取�?有需要建立索引的文件
		File[] files = new File(dataDirectory).listFiles();

		for (int i = 0; i < files.length; i++) {
			// 文件是第几个
			System.out.println("这是�?" + i + "个文�?----------------");
			// 文件的完整路�?
			System.out.println("完整路径�?" + files[i].toString());
			// 获取文件名称
			String fileName = files[i].getName();
			// 获取文件后缀名，将其作为文件类型
			String fileType = fileName.substring(fileName.lastIndexOf(".") + 1, fileName.length()).toLowerCase();
			// 文件名称
			System.out.println("文件名称�?" + fileName);
			// 文件类型
			System.out.println("文件类型�?" + fileType);

			Document doc = new Document();

			// String fileCode = FileType.getFileType(files[i].toString());
			// 查看各个文件的文件头标记的类�?
			// System.out.println("fileCode=" + fileCode);

			InputStream in = new FileInputStream(files[i]);
			InputStreamReader reader = null;

			if (fileType != null && !fileType.equals("")) {

				if (fileType.equals("doc")) {
					// 获取doc的word文档
					WordExtractor wordExtractor = new WordExtractor(in);
					// 创建Field对象，并放入doc对象�?
					// Field的各个字段含义如下：
					// �?1个参数是设置field的name�?
					// �?2个参数是value，value值可以是文本（String类型，Reader类型或�?�是预分享的TokenStream�?,
					// 二进制（byet[]�?, 或�?�是数字（一�? Number类型�?
					// �?3个参数是Field.Store，�?�择是否存储，如果存储的话在�?索的时�?�可以返回�??
					// �?4个参数是Field.Index，用来设置索引方�?
					doc.add(new Field("contents", wordExtractor.getText(), Field.Store.YES, Field.Index.ANALYZED));
					// 关闭文档
					wordExtractor.close();
					System.out.println("注意：已为文件�??" + fileName + "”创建了索引");

				} else if (fileType.equals("docx")) {
					// 获取docx的word文档
					XWPFWordExtractor xwpfWordExtractor = new XWPFWordExtractor(new XWPFDocument(in));
					// 创建Field对象，并放入doc对象�?
					doc.add(new Field("contents", xwpfWordExtractor.getText(), Field.Store.YES, Field.Index.ANALYZED));
					// 关闭文档
					xwpfWordExtractor.close();
					System.out.println("注意：已为文件�??" + fileName + "”创建了索引");

				} else if (fileType.equals("pdf")) {
					// 获取pdf文档
					PDFParser parser = new PDFParser(in);
					parser.parse();
					PDDocument pdDocument = parser.getPDDocument();
					PDFTextStripper stripper = new PDFTextStripper();
					// 创建Field对象，并放入doc对象�?
					doc.add(new Field("contents", stripper.getText(pdDocument), Field.Store.YES, Field.Index.ANALYZED));
					// 关闭文档
					pdDocument.close();
					System.out.println("注意：已为文件�??" + fileName + "”创建了索引");

				} else if (fileType.equals("txt")) {
					// 建立�?个输入流对象reader
					reader = new InputStreamReader(in);
					// 建立�?个对象，它把文件内容转成计算机能读懂的语�?
					BufferedReader br = new BufferedReader(reader);
					String txtFile = "";
					String line = null;

					while ((line = br.readLine()) != null) {
						// �?次读入一行数�?
						txtFile += line;
					}
					// 创建Field对象，并放入doc对象�?
					doc.add(new Field("contents", txtFile, Field.Store.YES, Field.Index.ANALYZED));
					System.out.println("注意：已为文件�??" + fileName + "”创建了索引");

				} else {

					System.out.println();
					continue;

				}

			}
			// 创建文件名的域，并放入doc对象�?
			doc.add(new Field("filename", files[i].getName(), Field.Store.YES, Field.Index.NOT_ANALYZED));
			// 创建时间的域，并放入doc对象�?
			doc.add(new Field("indexDate", DateTools.dateToString(new Date(), DateTools.Resolution.DAY),
					Field.Store.YES, Field.Index.NOT_ANALYZED));
			// 写入IndexWriter
			indexWriter.addDocument(doc);
			// 换行
			System.out.println();
		}
		// 查看IndexWriter里面有多少个索引
		System.out.println("numDocs=" + indexWriter.numDocs());
		// 关闭索引
		indexWriter.close();
	}

	public static void main(String[] args) {
		String dataPath = "D:\\test";
		String indexPath = "D:\\testik";
		try {
			creatIndex(dataPath, indexPath);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

