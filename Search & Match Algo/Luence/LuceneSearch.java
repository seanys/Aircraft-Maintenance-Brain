package com.luence.util;

import java.io.File;
import java.io.IOException;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.List;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.search.highlight.Highlighter;
import org.apache.lucene.search.highlight.InvalidTokenOffsetsException;
import org.apache.lucene.search.highlight.QueryScorer;
import org.apache.lucene.search.highlight.SimpleFragmenter;
import org.apache.lucene.search.highlight.SimpleHTMLFormatter;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;

public class LuceneSearch {

	public static List<Luence> search(String luenceIndex, String keyWord) throws IOException, ParseException {
		List<Luence> list = new ArrayList<Luence>();
		// 保存索引文件的地�?
		String indexDirectory = luenceIndex;
				// 创建Directory对象 ，也就是分词器对�?
				Directory dir = FSDirectory.open(new File(indexDirectory));
				IndexReader reader = DirectoryReader.open(dir);
				// 创建 IndexSearcher对象，相比IndexWriter对象，这个参数就要提供一个索引的目录就行�?
				IndexSearcher indexSearch = new IndexSearcher(reader);
				// 创建QueryParser对象,
				// �?1个参数表示Lucene的版�?,
				// �?2个表示搜索Field的字�?,
				// �?3个表示搜索使用分词器
				QueryParser queryParser = new QueryParser(Version.LUCENE_43, "contents",
						new StandardAnalyzer(Version.LUCENE_43));
				// 生成Query对象
		Query query = queryParser.parse(keyWord);
				// 搜索结果 TopDocs里面有scoreDocs[]数组，里面保存着索引�?
				TopDocs hits = indexSearch.search(query, 10);
				// hits.totalHits表示�?共搜到多少个
				System.out.println("找到�?" + hits.totalHits + "�?");
				// 循环hits.scoreDocs数据，并使用indexSearch.doc方法把Document还原，再拿出对应的字段的�?
				for (int i = 0; i < hits.scoreDocs.length; i++) {
			Luence luence = new Luence();
					ScoreDoc sdoc = hits.scoreDocs[i];
					Document doc = indexSearch.doc(sdoc.doc);
			// System.out.println(doc.get("filename"));
			// System.out.println(doc.get("contents"));
					String content = doc.get("contents");
					/* Begin:�?始关键字高亮 */
					SimpleHTMLFormatter formatter = new SimpleHTMLFormatter("<b><font color='red'>", "</font></b>");
					Highlighter highlighter = new Highlighter(formatter, new QueryScorer(query));
					highlighter.setTextFragmenter(new SimpleFragmenter(400));
					Analyzer luceneAnalyzer = new StandardAnalyzer(Version.LUCENE_30);
					if (content != null) {
				TokenStream tokenstream = luceneAnalyzer.tokenStream(keyWord, new StringReader(content));
						try {
							content = highlighter.getBestFragment(tokenstream, content);
						} catch (InvalidTokenOffsetsException e) {
							e.printStackTrace();
						}
					}
					/* End:结束关键字高�? */
			// System.out.println("文件内容:" + content);
			luence.setName(doc.get("filename"));
			luence.setContent(content);
			list.add(luence);
				}
				reader.close();
		return list;
	}

	public static void main(String[] args) {
		String indexPath = "D:\\testik";
		String keyword = "网站";
		try {
			List<Luence> list = search(indexPath, keyword);
			if (list.size() > 0) {
				for (Luence luence : list) {
					System.out.println("名称�?" + luence.getName());
					System.out.println("内容�?" + luence.getContent());
				}
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
