<template>
	<view>
		<view style="display: flex;flex-wrap: wrap">
			<navigator url="../component/component" class="cu-card " hover-class="none" style="max-width: 380px;" v-for="(item,index) in historySearch" :key="index">
				<view class="cu-item shadow" >
					<view style="width:330px;height:300px;background-size:cover;" :style="'background-image:url('+item['image_url']+');'"></view>
					<view class="cu-list menu-avatar">
						<view class="cu-item">
							<view class="content flex-sub">
								<view class="text-sm flex justify-between">
									<span style="font-size: bold;">Time:</span>{{item['upload_time']}}  
								</view>
							</view>
						</view>
					</view>
				</view>
			</navigator>
		</view>
	</view>
</template>

<script>
	import config from "../../common/config.js"
	export default {
		data() {
			return {
				historySearch:[]
			}
		},
		onLoad:function(){
			var that=this
			uni.request({
				url: config.service.host + '/weapp/aircraftuser',
				data: {
					user_id: 1
				},
				success:function(res){
					console.log(res)
					that.historySearch=res.data.data.infor
				}
			})
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
