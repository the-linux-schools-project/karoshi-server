function getCookieVal(name){var ca=document.cookie.split(';');var nameEQ=name+"=";for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==' ')c=c.substring(1,c.length);if(c.indexOf(nameEQ)==0)return c.substring(nameEQ.length,c.length)}return null}
function getRandom(num){var n=1000000000;function ugen(old,a,q,r,m){var t=Math.floor(old/q);
t=a*(old-(t*q))-(t*r);return Math.round((t<0)?(t+m):t);}var m1=2147483563,m2=2147483399,a1=40014,a2=40692,q1=53668,q2=52774,r1=12211,r2=3791,x=67108862;
var g2=(Math.round(((new Date()).getTime()%100000))&2147483647),g1=g2;var shuffle=[32],i=0;
for(;i<19;i++){g1=ugen(g1,a1,q1,r1,m1);}for(i=0;i<32;i++){g1=ugen(g1,a1,q1,r1,m1);
shuffle[31-i]=g1;}g1=ugen(g1,a1,q1,r1,m1);g2=ugen(g2,a2,q2,r2,m2);var s=Math.round((shuffle[Math.floor(shuffle[0]/x)]+g2)%m1);
var rand=Math.floor(s/(m1/(n+1)))/n;if(typeof(num)=="undefined"){return rand;}else{return Math.floor(rand*(num+1));
}}
var SR_url = window.location.toString().toLowerCase();
var _refv = escape(document.referrer);
var _rn = getRandom();
var smallScreenMatch = window.matchMedia("(max-width:" + 450 / 16 + "em)");
function loadCle(st, freq,_s,_l) {
		_freq = freq;
		checkCle = cleCookie();
		if(getCookieVal("tstCLE")==1){var c='tstCLE=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';	document.cookie=c; checkCle=true; _freq=100;}
		if(checkCle) {
			if( document.cookie.indexOf('msresearch') == -1 && !(/^http(s)?\:\/\/windows\.microsoft\.com/i.test(document.referrer)) ){ 
				if(_rn <= _freq){					
					if(st==1) {
						window.location.href = 'http://js.microsoft.com/library/svy/windows/int_cle.htm?location='+escape(window.location)+'&referrer='+_refv+'&frequency='+_freq+'&weight=100&site='+_s+'&SURVEY_TYPE=1&l='+_l;
					}					
				}
		}
	}
}
function cleCookie() {
		if(document.cookie.indexOf('cleflag') == -1) {
			var c = 'cleflag=1; path=/; domain=.microsoft.com';
			document.cookie = c;	
			return true;
		}else{
			var _v = getCookieVal('cleflag'); _v++;
			var c = 'cleflag='+_v+'; path=/; domain=.microsoft.com';
			document.cookie = c;	
			return false;
		}
}

if(!(/iphone|ipad|iphone|android|opera mini|blackberry|windows(phone|ce)|iemobile|htc|nokia/i.test(navigator.userAgent)) && !smallScreenMatch.matches){
if(/[\w\.]+\/en-us/i.test(SR_url)) {
	var _f = 0.0407, _l="9";
	if(/windows-8\/meet/i.test(SR_url)) {
		loadCle(1, 0.0122,"1992",_l);
	}else if(/windows-8\/new-pcs/i.test(SR_url)) {
		loadCle(1, _f,"1993",_l);	
	}else if(/windows\/pc-selector/i.test(SR_url)) {
		loadCle(1, 0.1,"1995",_l);	
	}else if(/windows-8\/new-look/i.test(SR_url)) {
		loadCle(1, _f,"2018",_l);	
	}else if(/windows-8\/work-play/i.test(SR_url)) {
		loadCle(1, _f,"2020",_l);	
	}else if(/windows-8\/compare/i.test(SR_url)) {
		loadCle(1, 0.1,"2176",_l);
	}
}else if(/[\w\.]+\/pt-br/i.test(SR_url)) {
	var _f = 0.1, _l="1046";
	if(/windows-8\/meet/i.test(SR_url)) {
		loadCle(1, _f,"2000",_l);
	}else if(/windows\/pc-selector/i.test(SR_url)) {
		loadCle(1, _f,"2003",_l);	
	}else if(/windows-8\/compare/i.test(SR_url)) {
		loadCle(1, _f,"2217",_l);	
	}else if(/windows-8\/honestly/i.test(SR_url)) {
		loadCle(1, _f,"2377",_l);	
	}
}else if(/[\w\.]+\/zh-cn/i.test(SR_url)) {
	var _f = 0.0278, _l="4";
	if(/windows-8\/meet/i.test(SR_url)) {
		loadCle(1, _f,"1996",_l);
	}else if(/windows\/pc-selector/i.test(SR_url)) {
		loadCle(1, _f,"1999",_l);
	}else if(/windows-8\/honestly/i.test(SR_url)) {
		loadCle(1, _f,"2376",_l);	
	}
}else if(/[\w\.]+\/ja-jp/i.test(SR_url)) {
	var _f = 0.0858, _l="17";
	if(/windows-8\/meet/i.test(SR_url)) {
		loadCle(1, _f,"2231",_l);
	}else if(/windows-8\/compare/i.test(SR_url)) {
		loadCle(1, _f,"2234",_l);	
	}else if(/windows\/pc-selector/i.test(SR_url)) {
		loadCle(1, _f,"2241",_l);	
	}else if(/windows-8\/honestly/i.test(SR_url)) {
		loadCle(1, _f,"2375",_l);	
	}			
}else if(/[\w\.]+\/es-mx/i.test(SR_url)) {
	var _f = 0.5, _l="2058";
	if(/windows-8\/meet/i.test(SR_url)) {
		loadCle(1, _f,"2220",_l);
	}else if(/windows-8\/compare/i.test(SR_url)) {
		loadCle(1, _f,"2223",_l);	
	}else if(/windows\/pc-selector/i.test(SR_url)) {
		loadCle(1, _f,"2230",_l);	
	}else if(/windows-8\/honestly/i.test(SR_url)) {
		loadCle(1, _f,"2378",_l);	
	}	
}
}