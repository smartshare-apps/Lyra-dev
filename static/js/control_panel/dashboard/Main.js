$(document).ready(function() {

bindElements();
bindEvents();


	


});


function bindElements(){

}

function bindEvents(){

}

function refreshPlot(event){
	var tile_id = event.data.tile_id;
	var plot_params = event.data.plot_params;

	console.log(plot_params);

	var selectorString = '[data-tileID="' + String(tile_id) + '"]';
	var plot_frame = $(".plot-frame"+selectorString);

	plot_frame.attr( 'src', '/actions/plot/'+tile_id+'?' + plot_params);



}