<template>
	<view id="app">
		<web-view :src='url'></web-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				url: ''
			}
		},
		onLoad: function(option) {
			console.log('manual onLoad.')
			let fileID = option.fileID
			let page = option.page
			if (fileID && page) {
				this.url = 'https://ly.inftime.cn/Manual.html?fileID=' + fileID + '&page=' + page
				console.log('manual url:', this.url)
			}
		},
	}
</script>

<style>
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}
</style>
