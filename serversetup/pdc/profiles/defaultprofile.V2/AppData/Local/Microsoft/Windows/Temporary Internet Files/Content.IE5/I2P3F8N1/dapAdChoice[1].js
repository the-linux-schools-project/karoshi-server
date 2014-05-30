<!--
/******** DAP Code ********/
if (typeof siteID == 'undefined') {var siteID=0;}
if (typeof bucketID == 'undefined') {var bucketID="";}
if (typeof hu == 'undefined') {var hu="";}
(function(rvr_id, mpserv, mpi, mpcrgif, mpck, mpcke, bangmpck, mpcrid, geozip, geocity, geostate, geodma, refdomain, geocontinent, geocountry, geoareacode, mpvce, mpvc, bangmpvc, mpcrw, mpcrh, mpcrflash, mpcrn, flashVersion, siteID, bucketID, ac_on, eng_on, ppal_on, hu, protocol){

var UTCoffset = 0;
var UTCdt = 0;
var aboveFold = 0;
var beats = new Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 45, 60, 75, 90, 105, 120, 150, 180, 210, 240, 270, 300);
var intID;
var M1 = 0;
var M2 = 0;
var mCl = 0;
var mCp = 0;
var mSt = 0;
var ustat = "";
var mpserv;
var back_up = 0;
var siteid;
var engTrackingServ = protocol + "//edpn.ebay.com/";
var smpvc = mpvc;
var smpck = mpck;
var mp_swver = 0;
var ntee = "";
var ntes = "";
var nted = "";
var ntep = "";
var ntest = "";
var ntec = "";
var nteu = "";
var aID = "";
var sID = "";
var uID = "";
var tc_flag = "";
var pageURL = (window.location != window.top.location) ? document.referrer : window.top.location.href;
if (typeof ar === 'undefined') {
    var ar = new Array();
    var int = new Array();
    ar[rvr_id] = 0;
} else {
    ar[rvr_id] = 0;
}

function foldCheck(rvr) {
    var obj = document.getElementById("foldcheck" + rvr);
    var windowHeight = 0;
    topValue = obj.offsetTop;
    adHeight = obj.offsetHeight;
    if (self.innerHeight) {
        windowHeight = self.innerHeight;
    } else if (document.documentElement && document.documentElement.clientHeight) {
        windowHeight = document.documentElement.clientHeight;
    } else if (document.body) {
        windowHeight = document.body.clientHeight;
    }
    if (topValue - (adHeight / 2) < windowHeight) {
        aboveFold = 1;
    } else aboveFold = 0;

}

Array.prototype.contains = function (obj) {
    var i = this.length;
    while (i--) {
        if (this[i] === obj) {
            return true;
        }
    }
    return false;
}

function heartbeat(rvr, m2, m1) {

    if (beats.contains(ar[rvr])) {
        if (ar[rvr] >= 300) clearInterval(int[rvr]);
        var engurl = engTrackingServ + "engagement?pulse=" + rvr + "|" + m2 + "|" + m1 + "|" + ar[rvr];
        document.getElementById('iframe' + rvr).setAttribute("src", engurl);

    }
    ar[rvr]++;

}

function mp_getDapVariables(query, ac) {
    try {
        var params = "";
        var vars = query.split("&");
        for (var i = 0; i < vars.length; i++) {
            var pair = vars[i];
            var nameval = pair.split("=");
            var name = (nameval.length > 0) ? nameval[0] : "";

            if (name == "ir_DAP_I131") {
                ustat = nameval[1];
            }
            if (name == "ff6") {
                aID = nameval[1];
            }
            if (name == "ff7") {
                sID = nameval[1];
            }
            if (name == "siteid") {
                if (typeof (siteID) == "undefined") {
                    var siteID = nameval[1];
                }
            } else if (((name.length > 7) && (name.substring(0, 7) == "ir_DAP_") && (name != "ir_DAP_I5")) || (name == "imp_id")) {
                params += pair + "&";
		   } else if (name == "ff18") {
                params += "ir_DAP_ff18="+nameval[1]+"&";
            } else {
                if (mSt == 48672 || mSt == 47596 || mSt == 45805 || mSt == 51244 || mSt == 48852) {
                    //MM only
                    if (name == "ff9") ntee = nameval[1]; //exch
                    //else if(name=="ff7") ntes=nameval[1]; //stid
                    else if (name == "ff7") nted = nameval[1]; //dom
                    else if (name == "ff19") ntep = nameval[1]; //pubid
                    else if (name == "ff8") ntest = nameval[1]; //strat
                    else if (name == "ff5") ntec = nameval[1]; //camp
                }
                if (mSt == 35272) {
                    //CHANGO only
                    ac = 0;
                    if (name == "ff8") nted = nameval[1]; //dom
                    else if (name == "ff9") nteu = nameval[1]; //encoded url
                }
            }
        }

        params += "ir_DAP_I5=" + ac + "&"
       if ((mSt == 35272) && (mCp=199402)) { params += "catID=" + sID + "&"}
        if (params.length > 0)
            params = params.substring(0, (params.length - 1));
        return params;
    } catch (err) {
        return "";
    }
    return "";
}

function mp_getMPVariables(ct, crid, zip, city, state, dma, refdom, continent, country, areacode) {
    try {
        var params = "";
        var pidreg = /\d+-\d+-\d+-\d+/;
        if (pidreg.test(ct)) {
            var pid = new String(ct.match(pidreg));
            var nameval = pid.split("-");
            mCl = (nameval.length > 0) ? nameval[0] : 0;
            mCp = (nameval.length > 1) ? nameval[1] : 0;
            mSt = (nameval.length > 2) ? nameval[2] : 0;
            pid = pid.replace(/\D/g, "");
        } else {
            var pid = new String("");
        }


        M1 = pid;
        M2 = crid;
        var M3 = (zip.indexOf("<g") >= 0) ? "" : zip;
        var M4 = (city.indexOf("<g") >= 0) ? "" : city;
        var M5 = (state.indexOf("<g") >= 0) ? "" : state;
        var M6 = (dma.indexOf("<g") >= 0) ? "" : dma;
        var M7 = (refdom.indexOf("<r") >= 0) ? "" : refdom;
        var M8 = (continent.indexOf("<g") >= 0) ? "" : continent;
        var M9 = (country.indexOf("<g") >= 0) ? "" : country;
        var M10 = (areacode.indexOf("<g") >= 0) ? "" : areacode;
        params += "ir_DAP_M0=" + isSecure + "&";
        params += "ir_DAP_M1=" + M1 + "&";
        params += "ir_DAP_M2=" + M2 + "&";
        params += "ir_DAP_M3=" + M3 + "&";
        params += "ir_DAP_M4=" + M4 + "&";
        params += "ir_DAP_M5=" + M5 + "&";
        params += "ir_DAP_M6=" + M6 + "&";
        params += "ir_DAP_M7=" + M7 + "&";
        params += "ir_DAP_M8=" + M8 + "&";
        params += "ir_DAP_M9=" + M9 + "&";
        params += "ir_DAP_M10=" + M10 + "&";
        if (typeof (siteID) != "undefined") {
            params += "ir_DAP_I6=" + siteID;
        }
        return params;
    } catch (err) {
        return "";
    }
    return "";
}


var dapParams = mp_getMPVariables(mpck, mpcrid, geozip, geocity, geostate, geodma, refdomain, geocontinent, geocountry, geoareacode) + "&dap3_template_id=" + mpcrid + "&rvr_id=" + rvr_id;
var dapVars = mp_getDapVariables(mpck, ac_on);
if (dapVars.length > 0) dapParams += "&" + dapVars;


var roverParams = (function () {
    for (var a = window.location.href, b = document.getElementsByTagName("script"), c = b.length; a.indexOf("rover.ebay") < 0 && c--;) a = b[c].getAttribute("src") || "";
    return b = {}, a.replace(/[?&]+([^=&]+)=([^&]*)/g, function (a, c, d) {
        b[c] = d
    }), b
})();

var ntfp = 1;
if (mSt == "51658") {
    ntfp = 0;
}

var adm_on = false;
if (!roverParams.adm || roverParams.adm == "" || roverParams.adm == "undefined" || roverParams.adm == null) {
	if (("-191106-191107-191108-200203-200204-200205-".indexOf("-" + mCp + "-") > -1)) {
		adm_on = true;
	} else if (("-707-709-710-724-1185-".indexOf("-" + mCl + "-") > -1)) {
		adm_on = Math.random() < 0.1;
	} else {
		adm_on = false;
	}
} else {
	adm_on = Math.random() < (1 / parseInt(roverParams.adm, 10));
}

if (adm_on) {
    // EU viewability tracking
    eng_on = 0;
    var am_host = (isSecure ? "https://secure-metrics.nt.vc" : "http://metrics.nt.vc"),
        am_src = am_host + "/metrics.js?ii=" + rvr_id + "&cn=foldcheck" + rvr_id + "&sz=" + mpcrw + "x" + mpcrh + "&cl=" + siteID + "&ee=" + ntee + "&es=" + ntes + "&dfp=" + ntfp + "&ed=" + nted + "&eu=" + nteu + "&ep=" + ntep + "&est=" + ntest + "&ec=" + ntec + "&pl=" + M1 + "&cr=" + M2 + "&hu=" + hu,
        am_script = '<scr' + 'ipt type="text/javascript" src="' + am_src + '"></scr' + 'ipt>';

    if (window.DocumentWrite) {
        DocumentWrite(am_script);
    } else {
        document.write(am_script);
    }
}

function addTag() {
    var  mp_html= "";

    if (navigator.mimeTypes && navigator.mimeTypes["application/x-shockwave-flash"] && navigator.mimeTypes["application/x-shockwave-flash"].enabledPlugin) {
        if (navigator.plugins && navigator.plugins["Shockwave Flash"]) {
            mp_swver = (navigator.plugins["Shockwave Flash"].description.split(" "))[2];
        }
    } else if (navigator.userAgent && navigator.userAgent.indexOf("MSIE") >= 0 && (navigator.userAgent.indexOf("Windows") >= 0)) {
        var mp_axo, e;
        for (var mp_i = 11; mp_i > 6; mp_i--) {
            try {
                mp_axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash." + mp_i);
                mp_swver = mp_i;
                break;
            } catch (e) {}
        }
    }

    if (mp_swver >= flashVersion) {
        mp_html = '<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" ';
        mp_html += ' codebase="https://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" id="' + mpcrid + '" name="movie' + mpcrid + '" width="' + mpcrw + '" height="' + mpcrh + '">';
        mp_html += '<param name="FlashVars" value="clickTAG=' + mpvc + mpck + '&clickTag=' + mpvc + mpck + '&clickTag1=' + mpvc + mpck + '&url=' + encodeURIComponent(encodeURIComponent(pageURL)) + '">';
        mp_html += '<param name="movie" value="' + mpserv + mpcrflash + '?' + dapParams + '">';
        mp_html += '<param name="wmode" value="opaque">';
        mp_html += '<param name="allowscriptaccess" value="always">';
        mp_html += '<embed wmode="opaque" allowscriptaccess="always" name="' + mpcrn + '" src="' + mpserv + mpcrflash + '?' + dapParams + '" FlashVars="clickTAG=' + mpvc + mpck + '&clickTag=' + mpvc + mpck + '&clickTag1=' + mpvc + mpck + '&url=' + encodeURIComponent(encodeURIComponent(pageURL)) + '"';
        mp_html += ' swLiveConnect="false" width="' + mpcrw + '" height="' + mpcrh + '" type="application/x-shockwave-flash" pluginspage="">';
        mp_html += '</embed>';
        mp_html += '</object>';
    } else {
        back_up = 1;
        mp_html = '<a href="' + smpvc + protocol + '//' + smpck + '&ff7=' + sID + '&ff1=' + aID + '&ff10=' + M2 + '" target="_blank"><img src="' + mpserv + mpcrgif + '" width="' + mpcrw + '" height="' + mpcrh + '" border="0" alt=""></a>';
    }
    var mydiv = document.getElementById("foldcheck" + rvr_id);
    var newcontent = document.createElement('div');
    newcontent.innerHTML = mp_html;
    while (newcontent.firstChild) {
        mydiv.appendChild(newcontent.firstChild);
    }
}

function logEng() {
    foldCheck(rvr_id);
    var iframe = document.createElement('iframe');
    iframe.setAttribute("id", "iframe" + rvr_id);
    iframe.setAttribute("width", "0");
    iframe.setAttribute("height", "0");
    iframe.setAttribute("border", "0");
    iframe.setAttribute("style", "width: 0; height: 0; border: none;");
    document.getElementById("foldcheck" + rvr_id).appendChild(iframe);

    var engurl = engTrackingServ + "engagement?INIT=" + rvr_id + "|" + M2 + "|" + M1 + "|" + aboveFold + "|" + mp_swver + "|" + back_up + "|" + tc_flag + "|" + uID + "|" + pageURL;
    iframe.setAttribute("src", engurl);

}
if (eng_on == 1) {
    logEng();
}
/******** DAP Code ********/
(function () {

    if (ppal_on == 1) {
        var tracerck = mpck.replace(/\/\d{1,2}\?/, "?");
        tracerck = tracerck.substr(23, tracerck.length);
        mpck = "altfarm.mediaplex.com/ad/ck/" + tracerck + "&ck=" + M2 + "-main&mpcr=" + M2 + "&ff7=" + sID + "&ff1=" + aID + "&ff10=" + M2;
        bangmpck = encodeURIComponent(mpck);
        var tracerar = "http://altfarm.mediaplex.com/ad/tr/" + tracerck + "&mpcr=" + M2 + "&ff7=" + sID + "&ff1=" + aID + "&ff10=" + M2;

        var tracerImg = new Image();
        tracerImg.style.width = "1px";
        tracerImg.style.height = "1px";
        tracerImg.style.border = "0px";
        tracerImg.src = tracerar;
    }

    if (mpvce == 1) {
        mpvclick = encodeURIComponent(mpvc);
        mpvc = mpvclick;
    } else if (mpvce == 2) {
        mpvclick2 = encodeURIComponent(mpvc);
        mpvclick2a = encodeURIComponent(mpvclick2);
        mpvc = mpvclick2a;
    } else {
        mpvc = (bangmpvc);
    }
    if (mpcke == 1) {
        mpcclick = encodeURIComponent("http://" + mpck + "&ir_DAP_M2=" + M2 + "&ff7=" + sID + "&ff1=" + aID + "&ff10=" + M2 + "&mpcr=" + M2);
        mpck = mpcclick;
    } else if (mpcke == 2) {
        mpcclick2 = encodeURIComponent("http://" + mpck + "&ir_DAP_M2=" + M2 + "&ff7=" + sID + "&ff1=" + aID + "&ff10=" + M2 + "&mpcr=" + M2);
        mpcclick2a = encodeURIComponent(mpcclick2);
        mpck = mpcclick2a;
    } else {
        mpck = "http://" + bangmpck + encodeURIComponent("&ir_DAP_M2=" + M2 + "&ff7=" + sID + "&ff1=" + aID + "&ff10=" + M2 + "&mpcr=" + M2);
    }

        addTag();
   })();
//Spring Campaign
if (("-29211079-27370136-27370140-27370143-27370146-27374812-27374758-27374756-27374816-27374782-27374780-27374778-27374820-27374770-27374768-27374766-27374822-27374764-27374762-27374760-27464167-27464165-27464163-27464161-27464159-".indexOf("-" + M2 + "-") > -1)) {
    var ne_script = '<scr' + 'ipt type="text/javascript"> (function () { var d = new Image(1, 1); d.onerror = d.onload = function () { d.onerror = d.onload = null; }; d.src = ["//secure-uk.imrworldwide.com/cgi-bin/m?ci=uk-ade2014-ca&at=view&rt=banner&st=image&ca=13303&ce=' + mSt + '&cr=' + M2 + '&pc=' + M1 + '&r=' + rvr_id + '"].join(\'\'); })();</scr' + 'ipt>';
    if (window.DocumentWrite) {
        DocumentWrite(ne_script);
    } else {
        document.write(ne_script);
    }
}
//DE C2C
else if (("-30182740-30182742-30182744-".indexOf("-" + M2 + "-") > -1)) {
    var ne_script = '<scr' + 'ipt type="text/javascript"> (function () { var d = new Image(1, 1); d.onerror = d.onload = function () { d.onerror = d.onload = null; }; d.src = ["//secure-uk.imrworldwide.com/cgi-bin/m?ci=uk-ade2014-ca&at=view&rt=banner&st=image&ca=13316&ce=' + mSt + '&cr=' + M2 + '&pc=' + M1 + '&r=' + rvr_id + '"].join(\'\'); })();</scr' + 'ipt>';
    if (window.DocumentWrite) {
        DocumentWrite(ne_script);
    } else {
        document.write(ne_script);
    }
}
//UK C2C
else if (("-30330683-30330681-30330679-30330677-".indexOf("-" + M2 + "-") > -1)) {
	if (mSt == "51242") {
    	var ne_script = '<scr' + 'ipt type="text/javascript"> (function () { var d = new Image(1, 1); d.onerror = d.onload = function () { d.onerror = d.onload = null; }; d.src = ["//secure-uk.imrworldwide.com/cgi-bin/m?ci=ENT21199&at=view&rt=banner&st=image&ca=cmp105717&ce=' + mSt + '&cr=' + M2 + '&pc=' + M1 + '&r=' + rvr_id + '"].join(\'\'); })();</scr' + 'ipt>';
	}
	else {
    	var ne_script = '<scr' + 'ipt type="text/javascript"> (function () { var d = new Image(1, 1); d.onerror = d.onload = function () { d.onerror = d.onload = null; }; d.src = ["//cdn.imrworldwide.com/cgi-bin/zp/7/z?ci=ENT21199&am=13&ep=1&at=view&rt=banner&st=image&ca=cmp105717&ce=' + mSt + '&cr=' + M2 + '&pc=' + M1 + '&r=' + rvr_id + '"].join(\'\'); })();</scr' + 'ipt>';
	}
    if (window.DocumentWrite) {
        DocumentWrite(ne_script);
    } else {
        document.write(ne_script);
    }
}

})(rvr_id, mpserv, mpi, mpcrgif, mpck, mpcke, bangmpck, mpcrid, geozip, geocity, geostate, geodma, refdomain, geocontinent, geocountry, geoareacode, mpvce, mpvc, bangmpvc, mpcrw, mpcrh, mpcrflash, mpcrn, flashVersion, siteID, bucketID, ac_on, eng_on, ppal_on, hu, protocol);

function getDap(rvrid) {
    return eval("dap" + rvrid);
}
//-->
