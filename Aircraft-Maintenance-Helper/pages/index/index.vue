<template>
	<view>
		<view class="weui-panel weui-panel_access" style="margin:25px 20px;background-color:transparent;">
			<navigator url="../detail/detail" class="weui-cell bg-white" style="border-radius:4px;margin-bottom:10px;padding:15px;position: relative;">
				<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
					<view class="weui-media-box__title">
						<span style="font-weight:bold;font-size:18px;margin-right: 9px;">HU7962</span>
						<span style="font-size:16px;color:#909399">B1543</span>
						<span style="float:right;font-size:16px;color:#4584EA;">Landing</span>
					</view>
					<view class="weui-media-box__desc" style="margin-top:5px;">
						<span style="margin-right:10px;">Runway：18L</span>
						<span style="margin-right:10px;">Position：269</span>
					</view>
				</view>
				<view class="weui-cell__ft weui-cell__ft_in-access"></view>
			</navigator>

			<navigator url="../detail/detail" class="weui-cell bg-white" style="border-radius:4px;margin-bottom:10px;padding:15px;position: relative;">
				<view class="weui-media-box__bd weui-media-box__bd_in-appmsg weui-cell__bd" style="width: 100%;">
					<view class="weui-media-box__title">
						<span style="font-weight:bold;font-size:18px;margin-right: 9px;">SQ827</span>
						<span style="font-size:16px;color:#909399">9VSYH</span>
						<span style="float:right;font-size:16px;color:#67C23A;">Under Maintenance</span>
					</view>
					<view class="weui-media-box__desc" style="margin-top:5px;">
						<span style="margin-right:10px;">Runway：18L</span>
						<span style="margin-right:10px;">Position：269</span>
					</view>
				</view>
				<view class="weui-cell__ft weui-cell__ft_in-access"></view>
			</navigator>
		</view>
	</view>
</template>

<script>
	import config from "../../common/config.js"
	export default {
		data() {
			return {
				navigatorBarColor: '#40485B',
				navigatorTitleColor: 'white',
				myCreate: "",
				border_array: ['normal_border_color', 'middle_border_color', 'important_border_color'],
				text_array: ['normal_color', 'middle_color', 'important_color'],
			}
		},
		components: {

		},
		onLoad() {
			this.loadBasic()
		},
		computed: {

		},
		methods: {
			loadBasic: function() {
				var that = this
			
			},
			navDetail: function(inf_id) {
				
			},
			detailUrl: function(inf_id) {
				
			}
		}
	}
</script>

<style>
	@import "../../common/weui.min.css";
	@import "../../common/basic.css";
	@import "../../common/inftime.css";
</style>
