<template>
	<view>
		<view class="page-body">
			<view class="page-section page-section-gap">
				<map style="width: 100%; height: 700px;" scale="14" :latitude="latitude" :longitude="longitude" :markers="covers">
				</map>
			</view>
		</view>
		<button @click="backIndex" style="margin:20px 20px;border-radius:23px;background-image: linear-gradient(-234deg, #499DF8 0%, #6EC3FC 100%);color:white;">
			查看完成
		</button>
	</view>
</template>

<script>
	import config from "../../common/config.js"
	export default {
		data() {
			return {
				navigatorTitle: "详情",
				nickname: "羊山",
				headImageUrl: "../../static/arrowLeftTopWhite.png",
				logged: true,
				achieve: false,
				itemImportance: 0,
				timeExit: true,
				widthCheckDetail: true,
				history: [],
				title: 'map',
				latitude: 31.1453899,
				longitude: 121.8006863,
				covers: [{
					latitude: 31.1453899,
					longitude: 121.8006863,
					iconPath: '../../../static/airplaneBlue.png'
				}]

			}
		},
		components: {

		},
		onLoad(options) {
			var that = this

		},
		computed: {

		},
		methods: {

			navComDetail: function() {
				uni.navigateTo({
					url: '../component/component'
				});
			},
			historyCheck: function() {

			},
			backIndex: function() {
				uni.navigateBack({
					delta: 1
				})
			},
		}
	}
</script>

<style>
	@import "../../common/weui.min.css";
	@import "../../common/basic.css";
	@import "../../common/inftime.css";
</style>
