<template>
	<view>
		<olmap />
	</view>
</template>

<script>
	import olmap from '@/components/olmap/olmap.vue'

	export default {
		data() {
			return {
				map: null
			}
		},
		components: {
			olmap
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>
	@import "../../common/weui.min.css";
	@import "../../common/basic.css";
	@import "../../common/inftime.css";
</style>
