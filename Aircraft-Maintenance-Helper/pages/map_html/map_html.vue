<template>
	<view>
		<web-view :webview-styles="webviewStyles" src="https://ly.inftime.cn/map.html"></web-view>
	</view>
</template>


<script>
	var wv;//计划创建的webview
	export default {
		data() {
			return {
				webviewStyles: {
					progress: {
						color: '#FF3333'
					}
				}
			}
		},
		onReady() {
			// // #ifdef APP-PLUS
			// var currentWebview = this.$mp.page.$getAppWebview() //获取当前页面的webview对象
			// setTimeout(function() {
			// 	wv = currentWebview.children()[0]
			// 	wv.setStyle({
			// 		height: 1300
			// 	})
			// }, 1000); //如果是页面初始化调用时，需要延时一下
			// // #endif
		}

	}
</script>

<style>
	@import "../../common/weui.min.css";
	@import "../../common/basic.css";
	@import "../../common/inftime.css";
</style>
