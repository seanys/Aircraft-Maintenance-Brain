<template>
	<view>
		<view class="weui-panel weui-panel_access" style="margin:20px 20px;background-color:transparent;" v-for="(maintenance,index) in history"
		 :key="maintenance.id">
			<view style="border-radius:4px;background-color: white!important;">
				<view class="weui-cell" style="padding:10px 20px;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;display: flex;">
						<view class="weui-media-box__title" style="display:flex;flex: 4;">
							<view style="font-size:16px;margin-right: 9px;" class="weui-cell__bd">
								<span style="margin-right:10px;font-weight:bold;text-transform: Uppercase;">{{maintenance['defect type']}}</span>
								<span style="margin-right:10px;color:#909399;font-size:15px;text-transform: Uppercase;">{{maintenance['check type']}}
									CHECK</span>
							</view>
						</view>
						<view style="text-align: right;flex: 1;color:rgb(69, 132, 234);" @click="detailDisplay(index)">{{maintenance['show_detail']}}</view>
					</view>
				</view>
				<view class="weui-cell" style="color:#606266;flex-wrap: wrap;line-height: 27px;" v-if="maintenance['show_detail']=='Expand'">
					<view>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);">INTRODUCTION </span>
						<span>{{'FROM ' +  maintenance.from+' TO '+maintenance.to+'; Defect Date: '+ maintenance['date'] +'; Completed By: '+maintenance['completion by date']+'; Defect Text: '+maintenance['defect text']}}</span>
					</view>
					<view style="color:#909399">{{maintenance['date']}}</view>
				</view>
				<view class="no-flex-cell" style="color:#606266;flex-wrap: wrap;line-height: 27px;" v-if="maintenance['show_detail']=='Collapse'">
					<view>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">from</span>
						<span style="margin-right: 10px;">{{maintenance['from']}}</span>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">to</span>
						<span style="margin-right: 10px;">{{maintenance['to']}}</span>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">description</span>
						<span>{{maintenance['description']}}</span>
					</view>
					<view>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">notification</span>
						<span>{{maintenance['notification']}}</span>
					</view>
					<view>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">priority</span>
						<span>{{maintenance['priority']}}</span>
					</view>
					<view>
						<span style="margin-right: 10px;color:rgb(69, 132, 234);text-transform: Uppercase;">defective components</span>
						<span v-for="(component,com_id) in maintenance['defective components']" :key="com_id" style="margin:10px;font-weight: bold;" @click="navComDetail">{{component}}</span>
					</view>
					<view>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">DEFECT DATE</span>
						<span style="margin-right: 20px;">{{maintenance['date']}}</span>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">COMPLETION BY DATE</span>
						<span>{{maintenance['completion by date']}}</span>
					</view>
					<view>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">ACTION</span>
						<span>{{maintenance['action']}}</span>
					</view>
					<view>
						<span style="margin-right: 5px;color:rgb(69, 132, 234);text-transform: Uppercase;">defect text</span>
						<span>{{maintenance['defect text']}}</span>
					</view>
				</view>
			</view>
		</view>

		<button @click="backIndex" style="margin:20px 20px;border-radius:23px;background-image: linear-gradient(-234deg, #499DF8 0%, #6EC3FC 100%);color:white;">	
		    View complete
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
				history: []
			}
		},
		components: {

		},
		onLoad(options) {
			var that = this
			uni.request({
				url: config.service.mock + '/flightlog/',
				data: {
					flightNumber: 861
				},
				success: function(res) {
					that.history = res.data.data.history
					for (var i = 0; i < that.history.length; i++) {
						if (i == 0) {
							that.history[i]['show_detail'] = "Collapse"
						} else {
							that.history[i]['show_detail'] = "Expand"
						}
					}
				}
			})

			uni.request({
				url: config.service.mock + '/manualproduct/',
				data: {
					productID: 10000
				},
				success: function(res) {
					console.log(res.data)
				}
			})
		},
		computed: {
			checkDetail: function() {
				return this.widthCheckDetail ? 0 : 90
			},
		},
		methods: {
			detailDisplay: function(e) {
				var maintenance = this.history[e]
				maintenance['show_detail'] = maintenance['show_detail'] == "Expand" ? "Collapse" : "Expand"
				this.$set(this.history, e, maintenance)
			},
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
