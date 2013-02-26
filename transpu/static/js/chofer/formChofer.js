$(function(){

	$("#demoForm").formwizard({ 
		formPluginEnabled: true,
		validationEnabled: true,
		historyEnabled: true,
		focusFirstInput : true,
		formOptions :{
			success: function(data){
				$("#status").fadeTo(500,1,function(){ $(this).html("You are now registered!").fadeTo(5000, 0); })
			},

			beforeSubmit: function(data){
				$("#data").html("data sent to the server: " + $.param(data));
			},
			
			dataType: 'json',
			resetForm: true
		}	
	});
	
	/*			
	$("#demoForm2").formwizard({ 
		formPluginEnabled: true,
		validationEnabled: true,
		historyEnabled: true,				 	
		focusFirstInput : true,
		formOptions :{
			success: function(data){
				$("#status2").fadeTo(500,1,function(){ $(this).html("You are now registered!").fadeTo(5000, 0); });
			},

			beforeSubmit: function(data){
				$("#data2").html("data sent to the server: " + $.param(data));
			},

			dataType: 'json',
			
			resetForm: true,
		}	
	});
	*/

});
