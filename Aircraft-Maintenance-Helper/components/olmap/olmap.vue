<template>
	<view id="map" ref="rootmap" style="height:800px;">
	</view>
</template>

<script>
	import "ol/ol.css";
	import {
		Map,
		View
	} from "ol";
	import TileLayer from "ol/layer/Tile";
	import OSM from "ol/source/OSM";
	export default {
		data() {
			return {
				map: null
			};
		},
		mounted() {
			var mapcontainer = this.$refs.rootmap;
			this.map = new Map({
				target: "map",
				layers: [
					new TileLayer({
						source: new OSM()
					})
				],
				view: new View({
					projection: "EPSG:4326", //使用这个坐标系
					center: [103.99,1.358], //樟宜机场
					zoom: 16
				})
			});
		}
	};
</script>

<style>
	#map {
		height: 100%;
	}

	/*隐藏ol的一些自带元素*/
	.ol-attribution,
	.ol-zoom {
		display: none;
	}
</style>
