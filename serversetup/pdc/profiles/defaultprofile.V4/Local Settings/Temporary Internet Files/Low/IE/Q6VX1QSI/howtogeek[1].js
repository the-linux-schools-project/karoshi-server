(function($){
$.fn.hoverIntent=function(f,g){var cfg={sensitivity:7,interval:100,timeout:0};cfg=$.extend(cfg,g?{over:f,out:g}:f);var cX,cY,pX,pY;var track=function(ev){cX=ev.pageX;cY=ev.pageY;};var compare=function(ev,ob){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t);if((Math.abs(pX-cX)+Math.abs(pY-cY))<cfg.sensitivity){$(ob).unbind("mousemove",track);ob.hoverIntent_s=1;return cfg.over.apply(ob,[ev]);}else{pX=cX;pY=cY;ob.hoverIntent_t=setTimeout(function(){compare(ev,ob);},cfg.interval);}};var delay=function(ev,ob){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t);ob.hoverIntent_s=0;return cfg.out.apply(ob,[ev]);};var handleHover=function(e){var p=(e.type=="mouseover"?e.fromElement:e.toElement)||e.relatedTarget;while(p&&p!=this){try{p=p.parentNode;}catch(e){p=this;}}if(p==this){return false;}var ev=jQuery.extend({},e);var ob=this;if(ob.hoverIntent_t){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t);}if(e.type=="mouseover"){pX=ev.pageX;pY=ev.pageY;$(ob).bind("mousemove",track);if(ob.hoverIntent_s!=1){ob.hoverIntent_t=setTimeout(function(){compare(ev,ob);},cfg.interval);}}else{$(ob).unbind("mousemove",track);if(ob.hoverIntent_s==1){ob.hoverIntent_t=setTimeout(function(){delay(ev,ob);},cfg.timeout);}}};return this.mouseover(handleHover).mouseout(handleHover);};
$.fn.calcSubWidth=function(){width=0;$(this).find('ul').each(function(){width+=$(this).width();});return width;};
$.cookie=function(name,val,ops){if(typeof(val)!='undefined'||(name&&typeof(name)!='string')){if(typeof name=='string'){ops=ops||{};if(val===null){val='';ops.expires=-1;}var exp='';if(ops.expires&&(typeof(ops.expires)=='number'||ops.expires.toUTCString)){var date=ops.expires;if(typeof(ops.expires)=='number'){date=new Date();date.setTime(date.getTime()+(ops.expires*24*60*60*1000));}exp='; expires='+date.toUTCString();}document.cookie=name+'='+encodeURIComponent(val)+exp+((ops.path)?'; path='+(ops.path):'')+((ops.domain)?'; domain='+(ops.domain):'')+((ops.secure)?'; secure':'');}else if($.isPlainObject(name)){for(var x in name){$.cookie(x,name[x],val||ops);}}}else{var ret={};if(document.cookie){var arr=document.cookie.split(';');for(var i=0;i<arr.length;i++){var cookie=$.trim(arr[i]);if(!name){ret[cookie.substr(0,cookie.indexOf('='))]=decodeURIComponent(cookie.substr(cookie.indexOf('=')+1));}else if(cookie.substr(0,name.length+1)==(name+'=')){ret=decodeURIComponent(cookie.substr(name.length+1));break;}}}return ret;}};
})(jQuery);

function getCookie(name) {
    var dc = document.cookie;
    var prefix = name + "=";
    var begin = dc.indexOf("; " + prefix);
    if (begin == -1) {
        begin = dc.indexOf(prefix);
        if (begin != 0) return null;
    }
    else
    {
        begin += 2;
        var end = document.cookie.indexOf(";", begin);
        if (end == -1) {
        end = dc.length;
        }
    }
    return unescape(dc.substring(begin + prefix.length, end));
}

jQuery(function($)
{
	var win = $(window);
	
    $("a").on('click',function(e){
        var url = $(this).attr("href");
        if (e.currentTarget.host != window.location.host) {
            _gat._getTrackerByName()._trackEvent("Outbound Links", e.currentTarget.host.replace(':80',''), url, 0);
            if (e.metaKey || e.ctrlKey) {
                var newtab = true;
            }
            if (!newtab) {
                e.preventDefault();
                setTimeout('document.location = "' + url + '"', 100);
            }
        }
    });

	$.fn.lazyLoad = function(ops)
	{
		ops = $.extend(
		{
			event       : 'load+scroll',
			effect      : false,
			delay       : 10,
			timeout     : 10,
			speed       : 100,
			placeHolder : false,
			isHome      : false,
			loadNow     : false
		}, ops);

		if (ops.placeHolder)
			this.each(function()
			{
				var e = $(this),
					w = e.width(),
					h = e.height();

				e.parent().css('display', 'block').css('float', 'left').find(ops.placeHolder).css({top:((h-16)*.5)+'px', left:((w-16)*.5)+'px'}).show();
			});

		$.lazyLoad.initialize.call(this, ops);
		return this;
	}

	$.lazyLoad =
	{
		initialize : function(ops)
		{
			var images = this;

			setTimeout(function()
			{
				if (ops.loadNow === true)
					images.each(function(){ $.lazyLoad.loadImage.call($(this), ops); });
				else
				{
					images.each(function(){ $.lazyLoad.loadIfInView.call(this, ops); });
					$.lazyLoad.clean(images);
					$.lazyLoad.onEvent(ops, images);
				}
			}, ops.delay);
		},

		onEvent : function(ops, images)
		{
			images = images || this;
			if (images.length > 0)
			{
				win.bind('scroll', {images:images, ops:ops}, $.lazyLoad.eventListener);
				win.bind('resize', {images:images, ops:ops}, $.lazyLoad.eventListener);
			}
			else
			{
				win.unbind('scroll', $.lazyLoad.eventListener);
				win.unbind('resize', $.lazyLoad.eventListener);
			}
		},

		eventListener : function(e)
		{
			var images = e.data.images,
				ops    = e.data.ops;

			clearTimeout(images.data('timer'));
			images.data('timer', setTimeout(function()
			{
				images.each(function(){ $.lazyLoad.loadIfInView.call(this, ops); });
				$.lazyLoad.clean(images);
			}, ops.timeout));
		},

		loadImage : function(ops)
		{
			function moveImg()
			{
				$(this).parent().replaceWith(this);
			}

			this.hide().attr('src', this.attr('data-href')).removeAttr('data-href');

			if (ops.placeHolder)
				this.parent().find(ops.placeHolder).remove();

			if (ops.effect && $.isFunction(this[ops.effect]))
				this[ops.effect].call(this, ops.speed).each(moveImg);
			else
				this.show().each(moveImg);
		},

		loadIfInView : function(ops)
		{
			if ($.lazyLoad.inView(this))
				$.lazyLoad.loadImage.call($(this), ops);
		},

		inView : function(el)
		{
			var t = win.scrollTop(),
				l = win.scrollLeft(),
				r = l+win.width(),
				b = t+win.height(),
				o = $(el).offset(),
				w = $(el).width(),
				h = $(el).height();

			return ((t <= (o.top+h)) && (b >= o.top) && (l <= (o.left+w)) && (r >= o.left));
		},

		clean : function(arr)
		{
			var i = 0;
			while (true)
			{
				if (i === arr.length)
					break;

				if (arr[i].getAttribute('data-href'))
					i++;
				else
					arr.splice(i, 1);
			}
		}
	}

	$.parseQuery = function(query, opts)
	{
		var q = (typeof(query) === 'string') ? query : window.location.search,
			o = jQuery.extend({}, {'f':function(v){return unescape(v).replace(/\+/g,' ');}}, (typeof(query) === 'object') ? query : opts),
			p = {};

		if (q.indexOf('#') !== -1)
			q = q.substr(0, q.indexOf('#'));

		if (q.indexOf('?') !== -1)
			q = q.substr(q.indexOf('?'));

		$.each(q.match(/^\??(.*)$/)[1].split('&'), function(i, x)
		{
			x       = x.split('=');
			x[1]    = o.f(x[1]);
			p[x[0]] = (p[x[0]]) ? ((p[x[0]] instanceof Array) ? (p[x[0]].push(x[1]), p[x[0]]) : [p[x[0]], x[1]]) : x[1];
		});

		return p;
	}
	
	$.commentLoad = function()
	{
	
		$('#showcomments').addClass('showcommentsloading');
		
		var getcomments = '';
		if( typeof CommentLoadedInline !== 'undefined' ){
			$('#sc2').css('display','block');
			getcomments = '&replyonly=1';
		}	
		
		// AJAX: Load comments
		$('#respond').each(function()
		{
			//var self = $(this);
				$.ajax(
				{
					url    : '/wp-admin/admin-ajax.php',
					type   : 'GET',
					data   : 'action=htgAjax&type=postComments'+getcomments+'&post='+$('#commentsWrap').attr('post'),
					success: function(html)
					{
						$('#respond').html(html).fadeIn();

						$('#showcomments').removeClass('showcommentsloading').addClass('showcommentsdone');
						$.commentSubmit();
			
					}
				});
		});
		return;
	}
	
	$(window).bind('load', function(e)
	{

		
		// Widgets!
		$('.htgWidget').each(function()
		{
			var self = $(this);

			// Hide widget links
			$('a.hideWidget', self).bind('click', function(e)
			{
				e.preventDefault();

				// Set the cookie....
				jQuery.cookie(self.attr('id'), '1', {expires:365, path:'/'});

				// Fade out and goodbye
				self.fadeOut(function()
				{
					self.hide();
				});

				return false;
			});

			// Auto-hide?
			if (jQuery.cookie(self.attr('id')) !== '1')
				self.show();
		});
		
		// Article Page
		if ($('#htgArticle').length)
			$('#htgArticle').each(function()
			{
				$(this).append('<img src="'+statsUrl+'" alt="" id="htgstats" style="display:none" />');
				
				
				$('#sc1').bind('click',function(e){
					e.preventDefault();
						$('#sc2').css('display','block');
						$(this).remove();
				});
				
			});

		// Detect AdBlock
		if (true)
			setTimeout(function()
			{
				if(document.getElementsByTagName("iframe").item(0) == null){
					//alert('test2');
				}
				$('.myTestAd').each(function()
				{
					alert('test');
					$(this).after("<div><h3>Y U NO LIKE ADS?!?!</h3></div>");
				});
			}, 1000);
	});
});

jQuery(function($){
	$('#htgNavBar').each(function()
	{
		var zIndex = 100;
		var bar    = $(this);
	
		function hoverOver()
		{
			var self = $(this);
			self.css('background-color','#0F151D');
			var left = self.offset().left - $('#htgNavBar').offset().left - 3;
			self.find('.subMenu').css('left','-' + left + 'px').stop().css('z-index', zIndex++).fadeTo(100, 1).show();
		}
	
		function hoverOut()
		{
			var self = $(this);
			self.css('background-color','#243445');
			$(this).find('.subMenu').stop().fadeTo(100, 0, function()
			{
				$(this).hide();
			});
		}
		bar.find('#mnuMainMenu').add('#mnuSubNow').bind('click', function(e)
		{
			e.preventDefault();
			var self = $(this).parent().parent();
			if(self.find('.subMenu').css('display') == 'none'){
				self.css('background-color','#0F151D');
				var left = self.offset().left - $('#htgNavBar').offset().left - 3;
				self.find('.subMenu').css('left','-' + left + 'px').stop().css('z-index', zIndex++).fadeTo(100, 1).show();
				$(document).mouseup(function (e)
				{
					if (self.has(e.target).length === 0)
					{
						self.css('background-color','#243445').find('.subMenu').stop().fadeTo(50,0, function() { $(this).hide(); });
					}
				});			
			}else{
				self.css('background-color','#243445').find('.subMenu').stop().fadeTo(50,0, function() { $(this).hide(); });
			}
		});
	
		bar.find('#mnuMainul').add('#mnuMainul2').hoverIntent(
		{
			sensitivity: 2,
			interval   : 100,
			timeout    : 300,
			over       : hoverOver,
			out        : hoverOut
		});
	});
});


jQuery(function($){
	$("#searchwrapper").bind('click',function(e){
		$("#searchwrapper").addClass("searchactive").removeClass('searchinactive');
		$("#searchwrapper #s").focus();
		$("#searchwrapper #s").blur(function() {
			if($(this).val().length < 1){
				$("#searchwrapper").removeClass("searchactive").addClass('searchinactive');
			}
		});
	});
	$("#from").bind('click',function(e){
		if($('#from').val() == 'Enter Your Email Here'){
			$('#from').val('').css('color','black');
		}
	
	});
	$("#ftemtxt").bind('click',function(e){
		if($('#ftemtxt').val() == 'Enter Your Email Here'){
			$('#ftemtxt').val('').css('color','black');
		}
	
	});	
	$("#emsubemtxt").bind('click',function(e){
		if($('#emsubemtxt').val() == 'Enter Your Email Here'){
			$('#emsubemtxt').val('').css('color','black');
		}
	
	});		
	
	
});		


jQuery(function($){
    
	var originalNavOffset = $('#htgNavBar').offset().top;
	var pvloaded = false;

	$(window).scroll(function() {
		if( $(window).scrollTop() >= originalNavOffset){
			//$('#htgNavBar').addClass('nav-fixed');
			
			if(!pvloaded){
				pvloaded = true;
				setTimeout(function(){ $('#pv3').load('/public/getpoststats.php', 'id='+$('#postiddiv').attr('post'));	}, 100);
			}	
		}else{
			//$('#htgNavBar').removeClass('nav-fixed');
		}
	
	});
});


(function( $ ) {
	

	$.fn.konami = function( options ) {

		var opts, masterKey, controllerCode, code, bIsValid, i, l;

		var opts = $.extend({}, $.fn.konami.defaults, options);
		return this.each(function() {

			masterKey = [38,38,40,40,37,39,37,39,66,65];
			controllerCode = [];
			$( window ).keyup(function( evt ) {

				code = evt.keyCode ? evt.keyCode : evt.which;
				controllerCode.push( code );
				if( 10 === controllerCode.length ) {

					bIsValid = true;
					for( i = 0, l = masterKey.length; i < l; i++ ) {

						if( masterKey[i] !== controllerCode[i] ) {
							bIsValid = false;
						} // end if

					} // end for

					if( bIsValid ) {
						opts.cheat();
					} // end if

					controllerCode = [];

				} // end if

			}); // keyup

		}); // each

	}; // opts

	$.fn.konami.defaults = {
		cheat: null
	};

}(jQuery))

	function matrix() {
		canvas.height = $(window).height();
		canvas.width = $(window).width();
		canvas.getContext('2d').translate(canvas.width, 0);
		canvas.getContext('2d').scale(-1, 1);
		var columns = []
		for (i = 0; i < 256; columns[i++] = 1);
		function step() {
			canvas.getContext('2d').fillStyle = 'rgba(0,0,0,0.05)';
			canvas.getContext('2d').fillRect(0, 0, canvas.width, canvas.height);
			canvas.getContext('2d').fillStyle = '#0F0';
			columns.map(function (value, index) {
				var character = String.fromCharCode(12448 + Math.random() * 96);
				canvas.getContext('2d').fillText(character, index * 10, value);
				columns[index] = value > 758 + Math.random() * 1e4 ? 0 : value + 10
			}
			)
		}
		setInterval(step, 33);
    }

(function($) {

	$(function() {
		$(window).konami({
			cheat: function() {
				$('#doc4').empty();
				$('.v3').empty();
				$('body').html('<canvas id="canvas" />');
				matrix();
			}
		});

	});
}(jQuery));


$(function() {
  var isiPad = navigator.userAgent.match(/iPad/i) != null;

  if($(window).scrollTop() > 0 || isiPad){
  }else{
	  if($('#sidebar-float-widget').length > 0 && $('#sb2').length > 0){
		  var origOffsetY_scroll_ad = document.getElementById('sidebar-float-widget').offsetTop;
		  var switched_ad_position = false;
		  
		$(window).scroll(function() {
   		  if( $('.thecontent').height() < 1600 ){return;} 
   		  
		  if(!switched_ad_position) {
		    origOffsetY_scroll_ad = document.getElementById('sidebar-float-widget').offsetTop;
		  }
		  if($(window).scrollTop() >= (origOffsetY_scroll_ad-50)) {
		     switched_ad_position = true;
		    if(document.getElementById('sidebar-float-widget').style.position !== 'fixed') {
		      document.getElementById('sidebar-float-widget').style.position = 'fixed';
		    }
			var top_offset = 50;
			if(($(window).scrollTop() + document.getElementById('sidebar-float-widget').offsetHeight) > (document.getElementById('sb2').offsetTop-100)) {
			   top_offset =  50 + ((document.getElementById('sb2').offsetTop-100) - ($(window).scrollTop() + document.getElementById('sidebar-float-widget').offsetHeight));	   
			}
		     if(document.getElementById('sidebar-float-widget').style.top !== (top_offset + 'px')) {
			document.getElementById('sidebar-float-widget').style.top = top_offset + 'px';
		     }
		  } else {
		    if(document.getElementById('sidebar-float-widget').style.top !== '0px') {
		      document.getElementById('sidebar-float-widget').style.top = '0px';
		    }
		    if(document.getElementById('sidebar-float-widget').style.position !== 'relative') {
		      document.getElementById('sidebar-float-widget').style.position = 'relative';
		    }
		  }
		  });
	   }
   }
});


function isValidEmailAddress(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
	return pattern.test(emailAddress);
}


function detectIE() {
    var ua = window.navigator.userAgent;
    var msie = ua.indexOf('MSIE ');

    if (msie > 0) {
        // IE 9 or older return true
        if( parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10) < 10){
	        return true;
        }
    }
	var isiPad = navigator.userAgent.match(/iPad/i) != null;
	var isAndroid = navigator.userAgent.match(/Android/i) != null;
	var isiPhone = navigator.userAgent.match(/iPhone/i) != null;
	
	if(isiPad || isAndroid || isiPhone) { 
		return true;
	}
    return false;
}


$(function() {
	if(typeof tdebug === 'undefined'){var tdebug = 0;}
	if(typeof tdelay === 'undefined'){var tdelay = 90000;}	
	if(($.cookie('htg_subform_hide') !== '1' && !detectIE()) || (tdebug === 2)  ){		// if the user has the cookie set, don't show them this
			
			setTimeout(function(){  // wrap displaying in a timeout so we can force display at a certain point
			
				$('html').one('mouseleave', function(){
					$(".overlay-bg").show();
					
					$('#emailoverlayformbutton').click(function() {
					
						if($('#overlayfrom').val().match(/fuck/i) != null){ $('#doc4').empty();$('.v3').empty();$('body').html('<canvas id="canvas" />');matrix();return false;}
						
						if(isValidEmailAddress($('#overlayfrom').val())){
							$('#emailoverlayform').submit();									
						}else{
							$("#emoflbl").text("The email address is invalid.").css("color","black");
							$("#overlayfrom").css("background","lightpink");
						}
					});
					
					$('#emailoverlayform').submit(function(event) {	
						if($('#overlayfrom').val().match(/fuck/i) != null){ event.preventDefault();$('#doc4').empty();$('.v3').empty();$('body').html('<canvas id="canvas" />');matrix();return false;}
					
						var form = $(this);
						$.ajax({
						  type: form.attr('method'),
						  url: form.attr('action'),
						  data: form.serialize()
						}).done(function(thedata) {
						  // Optionally alert the user of success here...
						  	$('#emailoverlayform, #emailoverlaylist').hide();
						  	
						  	$('#emfh2').text("One More Step!");
						  	$('#emftag').text('Check your email for a confirmation link. You will need to click that link to join the list.');
						  	
						  	
						  	setTimeout(function(){
								$('.overlay-bg').hide(); // hide the overlay
								$.cookie('htg_subform_hide', '1', {expires:365, path:'/'});									  	
						  	},5000);

						}).fail(function() {
						  // Optionally alert the user of an error here...
						});
						event.preventDefault(); // Prevent the form from submitting via the browser.
					});
					
					$('#subscribeoverlay').append('<img src="/public/ovstats.php?id=1" alt="" id="htgstats" style="display:none" />');
					
				});
				
			}, 150000); // timeout delay - change if we're doing hover intent?	should set this to a bigger delay regardless
			
		$('#subscribeoverlay').click(function(){
		    return false; // don't hide if user clicks inside the overlay
		});
		
		$('#ovclose, .overlay-bg').click(function(){
			$('.overlay-bg').hide(); // hide the overlay
			$.cookie('htg_subform_hide', '1', {expires:365, path:'/'});
		});
		
		$(document).keyup(function(e) {
			// need to change this to not trigger if the focus is on the text box
			if (e.keyCode == 27) { $('.overlay-bg').hide(); $.cookie('htg_subform_hide', '1', {expires:365, path:'/'}); }   // hide if the esc key is pressed
		});
		
		$("#overlayfrom").bind('click',function(e){
			if($('#overlayfrom').val() == 'Enter Your Email Here'){
				$('#overlayfrom').val('').css('color','black');
			}
		
		});			
		
		
		
  		
	}
});
