

var onAfterChange = function (value) {
	console.log("value: ", value);
};

ReactDOM.render(<ReactSlider 
	defaultValue={0}
	max={354}
	className='horizontal-slider'
	onAfterChange={onAfterChange}
	withBars />, document.getElementById('slider'));