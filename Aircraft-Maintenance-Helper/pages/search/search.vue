<template>
	<view>
		<view class="cu-bar search bg-white" style="position: fixed;top:0px;width: 100%;z-index: 2000;border-bottom:#E4E7ED solid 1px">
			<view class="search-form round" style="margin:10px 20px;">
				<text class="cuIcon-search"></text>
				<input type="text" focus="true" value="gear" @input="inputKeyword" @confirm="updateRec" confirm-type="search" style="font-size: 16px;height: 32px;"
				 :placeholder="searchTitle" />
			</view>
		</view>
		<view style="height:50px;"></view>
		<view class="weui-panel weui-panel_access" style="margin:20px 20px 10px 20px;background-color:transparent;">
			<view v-if="range_index==0">
				<view class="weui-cell" v-for="(searchRec,index) in AMMRecs" :key="index" v-if="AMMRecs.length>0&&searchRec['level']==level_index+1"
				 style="border-radius:4px;margin-bottom:10px;padding:10px 10px;position: relative;background-color: white;">
					<navigator @click="console.log(searchRec['url'])" url="../manual/manual?fileID=Boeing747_AMM_32_12&page=1"
					 class="weui-panel weui-panel_access" style="margin:10px 20px;background-color:transparent;">
						<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
							<view class="weui-media-box__title">
								<span style="font-size:18px;margin-right: 9px;">{{AMMRecs[index]['intro']}}</span>
							</view>
							<view class="weui-media-box__desc" style="margin-top:5px;font-size: 16px;">
								<!-- How to connect prediction algorithm is testing now -->
								<span style="margin-right: 20px;color:#4688F1" v-if="index==1||index==5||index==19">High probability</span>
								<span style="margin-right: 20px;color:#6AC044" v-if="index==2||index==7||index==10">Middle probability</span>
								<span>{{AMMRecs[index]['position']}} </span>
								
								<!-- {{searchRec['intro']}} -->
							</view>
						</view>
					</navigator>
				</view>
				<view v-if="arrayLength[level_index]==0" style="text-align: center;margin-top: 80px;font-size: 20px;color: #909399;">No
					result</view>
			</view>
			<view v-if="range_index==1">
				<view v-if="IPCRecs.length>0" class="weui-cell" v-for="(searchRec,index) in IPCRecs" :key="index" style="border-radius:4px;margin-bottom:10px;padding:10px 10px;position: relative;background-color: white;">
					<navigator @click="console.log(searchRec['url'])" url="../manual/manual?fileID=0a4ae825a3de4bdb25379ec48e06993c&page=6"
					 class="weui-panel weui-panel_access" style="margin:10px 20px;background-color:transparent;">
						<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
							<view class="weui-media-box__title">
								<span style="font-size:18px;margin-right: 9px;">{{searchRec['name']}}</span>
								<span style="font-size:16px;color:#909399">{{searchRec['code']}}</span>
							</view>
							<view class="weui-media-box__desc" style="margin-top:5px;font-size: 16px;">
								{{searchRec['note']}}
							</view>
						</view>
					</navigator>
				</view>
				<view v-if="IPCRecs.length==0" style="text-align: center;margin-top: 80px;font-size: 20px;color: #909399;">No
					result</view>
			</view>
			<view v-if="range_index==2" style="text-align: center;margin-top: 80px;font-size: 20px;color: #909399;">Function
				Developing</view>
			<view style="height:100px;"></view>
		</view>
		<view class="cu-bar bg-white tabbar border shop" style="bottom: 0px; position: fixed; width: 100%;font-size: 18px;border-top:#E4E7ED solid 1px">
			<view class="submit" @click="rangeIndexChang" style="border-right: #E4E7ED 1px solid;">
				<view class="uni-input">{{searchRange[range_index]}}</view>
				<text class="cuIcon-triangledownfill" style="font-size:30px;"></text>
			</view>
			<view class="submit" @click="levelIndexChang" v-if="range_index==0">
				<view class="uni-input">{{searchLevel[level_index]}}</view>
				<text class="cuIcon-triangledownfill" style="font-size:30px;"></text>
			</view>
			<view class="submit" @click="levelIndexChang" v-if="range_index>0">
				<view class="uni-input">Default</view>
			</view>
		</view>
	</view>
</template>

<script>
	import config from "../../common/config.js"
	export default {
		data() {
			return {
				logged: true,
				searchRange: ['AMM', 'IPC', 'Job Card'],
				searchLevel: ['Chapter', 'Section', 'Subject', 'Pageblock', 'Task'],
				arrayLength: [0,0,0,0,0],
				range_index: 0,
				level_index: 4,
				searchTitle: "Search AMM Manual",
				IPCRecs: [{
					"name": "MAINT ENTRY DUCT ASSY",
					"code": "390043",
					"note": "1 pcs half-finished ready for installation",
					"url": '../manual/manual?fileID=0a4ae825a3de4bdb25379ec48e06993c&page=6'
				}],
				AMMRecs: [{
					"intro": "MAINT ENTRY DUCT ASSY",
					// "probability": "Big Probability",
					// "intro": "PN: L9871230AZ IPC 36-12-42-01 ITEM 300B CANNIBALIZED TOSERVICE 2Q-QK7.",
					position: "32-33-31",
					"url": '../manual/manual?fileID=0a4ae825a3de4bdb25379ec48e06993c&page=6'
				}],
				keyword: "gear",
				history: [],
				firstClick: true,
				search_type: "AMM",
				from_detail:false
			}
		},
		components: {

		},
		onLoad(options) {
			var that = this
			that.updateRec()
			if(options.search_aircraft){
				that.from_detail=true
			}
		},
		computed: {

		},
		methods: {
			processStr: function(str, times) {
				var that = this
				if (times > 0) {
					times = times - 1
					var index = str.indexOf("-")
					str = str.substring(index + 1, str.length)
					return that.processStr(str, times)
				}
			},
			updateAMMDetail: function() {
				var that = this
				var newArrrayLength=[0,0,0,0,0]
				for (var i = 0; i < that.AMMRecs.length; i++) {
					var index = 23
					if (that.AMMRecs[i]['level'] == 5) {
						index = 22
						newArrrayLength[4]=newArrrayLength[4]+1
					}
					if (that.AMMRecs[i]['level'] == 4) {
						index = 23
						newArrrayLength[3]=newArrrayLength[3]+1
					}
					if (that.AMMRecs[i]['level'] == 3) {
						index = 17
						newArrrayLength[2]=newArrrayLength[2]+1
					}
					if (that.AMMRecs[i]['level'] == 2) {
						newArrrayLength[1]=newArrrayLength[1]+1
						index = 14
					}
					if (that.AMMRecs[i]['level'] == 1) {
						newArrrayLength[0]=newArrrayLength[0]+1
						index = 11
					}
					var str = that.AMMRecs[i]['intro']
					var position = str.substring(0, index);
					that.AMMRecs[i]['position'] = position
					var intro = str.substring(index + 2, str.length);
					that.AMMRecs[i]['intro'] = intro
					if(i==that.AMMRecs.length-1){
						console.log(newArrrayLength )
						that.arrayLength=newArrrayLength
					}
				}
				
			},
			updateRec: function() {
				var that = this
				console.log("update begin")
				if (that.keyword == "") {
					uni.showModal({
						title: 'Remind',
						content: 'Please input keywords you want to search',
						showCancel: false,
						success: function(res) {

						}
					});
				} else {
					uni.showToast({
						title: 'Loading',
						icon: "loading"
					});
					uni.request({
						url: config.service.host + '/weapp/amm',
						data: {
							keyword: that.keyword
						},
						success: function(res) {
							console.log(res.data)
							that.AMMRecs = res.data.data.infor
							that.updateAMMDetail()
							uni.hideToast();
						}
					})
					uni.request({
						url: config.service.host + '/weapp/ipc',
						data: {
							keyword: that.keyword
						},
						success: function(res) {
							that.IPCRecs = res.data.data.infor
							console.log(res.data)
						}
					})

				}
			},
			remindDevelop: function() {
				uni.showModal({
					title: 'Remind',
					content: 'We are developing this function',
					showCancel: false,
					success: function(res) {

					}
				});
			},
			levelIndexChang: function() {
				if (this.level_index < 4) {
					this.level_index = 1 + this.level_index
				} else {
					this.level_index = 0
				}
				// this.remindClickChange()
			},
			rangeIndexChang: function() {
				if (this.range_index < 2) {
					this.range_index = 1 + this.range_index
				} else
					this.range_index = 0
				this.searchTitle = "Search " + this.searchRange[this.range_index] + " Manual"
				// this.remindClickChange()
			},
			loadAMM: function() {

			},
			loadIPC: function() {

			},
			loadJobCard: function() {

			},
			remindClickChange: function() {
				if (this.firstClick) {
					uni.showModal({
						title: 'Introduction',
						content: 'You can click bottom tabbar to change search range',
						showCancel: false,
						success: function(res) {

						}
					})
					this.firstClick = false
				}
			},
			navDetail: function() {
				var that = this
				console.log(that.search_type)
				if (that.search_type == "AMM") {
					uni.openDocument({
						filePath: "https://ly.inftime.cn/Illustrated-parts-catalog.pdf",
						success: function(res) {
							console.log('打开文档成功');
						}
					})
				} else {
					uni.navigateTo({
						url: '../component/component'
					});
				}
			},
			bindPickerChange: function(e) {
				console.log('picker发送选择改变，携带值为', e.target.value)
				this.index = e.target.value
			},
			historyCheck: function() {

			},
			allHistory: function() {
				remindDevelop()
			},
			backIndex: function() {
				uni.navigateBack({
					delta: 1
				})
			},
			inputKeyword: function(e) {
				console.log(e)
				var that = this
				that.keyword = e.detail.value
			}
		}
	}
</script>

<style>
	@import "../../common/weui.min.css";
	@import "../../common/basic.css";
	@import "../../common/inftime.css";

	input::placeholder {
		font-size: 13px !important;
	}
</style>
