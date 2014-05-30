var _Freq=false;
var _halt=false; 
var _NavHalt = false;
var MSNavChannel=false;
var _newProjWeight = 100, _oldProjWeight = 0; //Default weights
var _surl = document.location.toString();
var A=document.getElementsByName("MS.Nav.Channel");

if(typeof(A[0])!="undefined"&&A[0]!=null){
 MSNavChannel="MS.Nav.Channel="+A[0].getAttribute("content");
   //var _t =  var _t = COMSCORE.SiteRecruit.Broker.findPageMapping(); 
   //if(typeof(_t)!="undefined" && _t !=null && typeof(_t.prereqs)!="undefined" && _t.prereqs!=null){	
if(/windows\.microsoft\.com\/en-us/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0436;
		}
	}else if(/windows\.microsoft\.com\/en-ca/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0563; 
		}
	}else if(/windows\.microsoft\.com\/en-gb/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0143;
		}
	}else if(/windows\.microsoft\.com\/en-au/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0636;
		}
	}else if(/windows\.microsoft\.com\/ja-jp/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0399; 
		}
	}else if(/windows\.microsoft\.com\/de-de/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0138; 
		}
	}else if(/windows\.microsoft\.com\/fr-fr/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0106; 
		}
	}else if(/windows\.microsoft\.com\/zh-cn/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0468;  
		}
	}else if(/windows\.microsoft\.com\/ko-kr/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0600; 
		}
	}else if(/windows\.microsoft\.com\/ru-ru/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0112; 
		}
	}else if(/windows\.microsoft\.com\/pt-br/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0665; 
		}
	}else if(/windows\.microsoft\.com\/es-mx/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.5; 
		}
	}else if(/windows\.microsoft\.com\/it-it/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0206;
		}
	}else if(/windows\.microsoft\.com\/tr-tr/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0461;
		}
	}else if(/windows\.microsoft\.com\/nl-nl/i.test(_surl)){
		if(/(home|Meet|Download-Shop|How-To|Support)/i.test(MSNavChannel)){
			_Freq=0.0445;
		}
	}
 }else{MSNavChannel=false;}
 if(/(zh-cn|pt-br|es-mx|ja-jp)\/windows\-8\/(features|honestly)/i.test(_surl)){_NavHalt=false;}else if(!_Freq){ _NavHalt=true; }
COMSCORE.SiteRecruit.Broker.config={version:"5.0.3",testMode:false,cookie:{name:"msresearch",path:"/",domain:".microsoft.com",duration:90,rapidDuration:0,expireDate:""},thirdPartyOptOutCookieEnabled:false,prefixUrl:"",Events:{beforeRecruit:function(){}},mapping:[{m:"//[\\w\\.-]+/de-de",c:"inv_c_p176052898-DE-DE.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/en-au",c:"inv_c_p176052898-EN-AU.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/en-ca",c:"inv_c_p176052898-EN-CA.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/en-gb",c:"inv_c_p176052898-EN-GB.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/en-us/",c:"inv_c_p176052898-US.js",f:_Freq,p:1,halt:_NavHalt},{m:"//[\\w\\.-]+/en-us/internet-explorer/products/ie-9/welcome$|welcome\\-upgrade|welcome\\-upgrade2",c:"inv_c_blank.js",f:0,p:0,halt:true},{m:"//[\\w\\.-]+/en-US/windows/pc-selector",c:"inv_c_p178132240-EN-US-pc-selector.js",f:0.5,p:2},{m:"//[\\w\\.-]+/en-us/windows7/(products/anytime-upgrade-(reg|none|change-settings|n)|sync-providers|search)",c:"inv_c_blank.js",f:0,p:0,halt:true},{m:"//[\\w\\.-]+/en-US/windows-8/compare",c:"inv_c_p178132240-EN-US-compare.js",f:0.5,p:2},{m:"//[\\w\\.-]+/en-US/windows-8/meet",c:"inv_c_p178132240-EN-US-meet.js",f:0.5,p:2},{m:"//[\\w\\.-]+/es-mx",c:"inv_c_p176052898-ES-MX.js",f:_Freq,p:1,halt:_NavHalt},{m:"//[\\w\\.-]+/es-mx/windows/pc-selector",c:"inv_c_p178132240-ES-MX-pc-selector.js",f:0.5,p:2},{m:"//[\\w\\.-]+/es-mx/windows-8/compare",c:"inv_c_p178132240-ES-MX-compare.js",f:0.5,p:2},{m:"//[\\w\\.-]+/es-mx/windows-8/honestly",c:"inv_c_p178132240-ES-MX-honestly.js",f:0.5,p:2},{m:"//[\\w\\.-]+/es-mx/windows-8/meet",c:"inv_c_p178132240-ES-MX-meet.js",f:0.5,p:2},{m:"//[\\w\\.-]+/fr-fr",c:"inv_c_p176052898-FR-FR.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/it-it",c:"inv_c_p176052898-IT-IT.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/ja-jp",c:"inv_c_p176052898-JA-JP.js",f:_Freq,p:1,halt:_NavHalt},{m:"//[\\w\\.-]+/ja-jp/windows/pc-selector",c:"inv_c_p178132240-JA-JP-pc-selector.js",f:0.5,p:2},{m:"//[\\w\\.-]+/ja-jp/windows-8/compare",c:"inv_c_p178132240-JA-JP-compare.js",f:0.5,p:2},{m:"//[\\w\\.-]+/ja-jp/windows-8/honestly",c:"inv_c_p178132240-JA-JP-honestly.js",f:0.5,p:2},{m:"//[\\w\\.-]+/ja-jp/windows-8/meet",c:"inv_c_p178132240-JA-JP-meet.js",f:0.5,p:2},{m:"//[\\w\\.-]+/ko-kr",c:"inv_c_p176052898-KO-KR.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/nl-nl",c:"inv_c_p176052898-NL-NL.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/pt-br",c:"inv_c_p176052898-PT-BR.js",f:_Freq,p:1,halt:_NavHalt},{m:"//[\\w\\.-]+/pt-BR/windows/pc-selector",c:"inv_c_p178132240-PT-BR-pc-selector.js",f:0.5,p:2},{m:"//[\\w\\.-]+/pt-BR/windows-8/compare",c:"inv_c_p178132240-PT-BR-compare.js",f:0.5,p:2},{m:"//[\\w\\.-]+/pt-BR/windows-8/honestly",c:"inv_c_p178132240-PT-BR-honestly.js",f:0.5,p:2},{m:"//[\\w\\.-]+/pt-BR/windows-8/meet",c:"inv_c_p178132240-PT-BR-meet.js",f:0.5,p:2},{m:"//[\\w\\.-]+/ru-ru",c:"inv_c_p176052898-RU-RU.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/tr-tr",c:"inv_c_p176052898-TR-TR.js",f:_Freq,p:4,halt:_NavHalt},{m:"//[\\w\\.-]+/zh-cn",c:"inv_c_p176052898-ZH-CN.js",f:_Freq,p:1,halt:_NavHalt},{m:"//[\\w\\.-]+/zh-cn/windows/pc-selector",c:"inv_c_p178132240-ZH-CN-PC-Sel.js",f:0.5,p:2},{m:"//[\\w\\.-]+/zh-cn/windows-8/compare",c:"inv_c_p178132240-ZH-CN-compare.js",f:0.5,p:2},{m:"//[\\w\\.-]+/zh-cn/windows-8/honestly",c:"inv_c_p178132240-ZH-CN-honestly.js",f:0.5,p:2},{m:"//[\\w\\.-]+/zh-cn/windows-8/meet",c:"inv_c_p178132240-ZH-CN-meet.js",f:0.5,p:2},{m:"[\\w\\.-]+/[\\w-]+/((internet-explorer/products/ie-9/(welcome|welcome-upgrade|welcome-upgrade2))|(windows7/(products/anytime-upgrade-(reg|none|change-settings|n)|sync-providers|search)))",c:"inv_c_blank.js",f:0,p:5,halt:true},{m:"/((es-es)|(it-it)|(tr-tr)|(nl-nl))/((internet-explorer/products/ie-9/(welcome|welcome-upgrade|welcome-grade2))|(windows7/(products/anytime-upgrade-(reg|none|change-settings|n)|sync-providers|search)))",c:"inv_c_blank.js",f:0,p:0,halt:true}]};
COMSCORE.SiteRecruit.Broker.run();