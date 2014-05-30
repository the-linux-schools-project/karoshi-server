document.write('');

(function() {
  var DEBUG = ''.toLowerCase() == 'true';
  var csiStart = (+new Date);
  var studioObjects = window['studioV2'] = window['studioV2'] || {};
  var publisherSideFilePath = '';
  if(publisherSideFilePath == '') {
    publisherSideFilePath = '/doubleclick/DARTIframe.html';
  } else if (publisherSideFilePath.charAt(publisherSideFilePath.length - 1) == '/') {
    publisherSideFilePath += 'DARTIframe.html';
  }
  var bookingTimeMetaData = {
    'useCookie': 'true'
  };

  var runtimeMetaData = {
  };

  var exitUrlPatternMacroValues = {
  };
  var macroParser = function (macroName, value) {
    return (value.indexOf(macroName) < 0) ? value : '';
  };
  var adServerData = {
    eventReportingUrl: 'http://ad-emea.doubleclick.net/activity;src=2567310;met=1;v=1;pid=108944397;aid=282155287;ko=0;cid=58179749;rid=58068862;rv=1;',
    clickUrl: 'http://wrapper.g.msn.com/GRedirect.aspx?g.msn.com/2AD000EJ/120000000000191760.1?!&&PID=12048056&UIT=G&TargetID=56063534&N=439354145&PG=UK9SV1&ASID=e0567c73b7b849cc98cf59e5f818a761&ANID=&MUID=3B046F88F0DF64FA24E469C0F4DF664C&destination=http://ad-emea.doubleclick.net/click%3Bh%3Dv8/3f5d/17/ec/%2a/v%3B282155287%3B0-0%3B0%3B108944397%3B43183-970/31%3B58179749/58068862/1%3B%3B%7Esscs%3D%3f',
    clickUrlTimesToEscape: '0',
    impressionUrl: 'http://ad-emea.doubleclick.net/imp;v7;j;282155287;0-0;0;108944397;970/31;58179749/58068862/1;;~cs=h%3f',
    geoData: 'ct=UK&st=&ac=114&zp=&bw=3&dma=0&city=3776',
    siteName: 'N4022.MSN',
    siteId: '600303',
    adId: '282155287',
    buyId: '8120932',
    creativeId: '58179749',
    placementId: '108944397',
    advertiserId: '2567310',
    keyValueOrdinal: '0',
    renderingVersion: '1',
    renderingId: '58068862',
    randomNumber: '2159714',
    dynamicData: '',
    stringReportingUrl: 'http://ad-emea.doubleclick.net/activity;src=2567310;stragg=1;v=1;pid=108944397;aid=282155287;ko=0;cid=58179749;rid=58068862;rv=1;rn=2159714;',
    urlToGetKeywordsFor: '%LivePreviewSiteUrl',
    bookingTimeMetaData: bookingTimeMetaData,
    exitSuffix: macroParser('exit_suffix', '%exit_suffix!'), // XFA GA Beacon.
    generatedAdSlot: false,
    exitUrlPatternMacroValues: exitUrlPatternMacroValues,
    activeViewClkStr: macroParser('eav', '%eav!'),
    renderingEnvironment: ('' == '1' ||
        window['mraid']) ? 'IN_APP' : 'BROWSER',
    placementDimensions: {
      'w': '%ew!',
      'h': '%eh!'
    },
    tag: {
      adContainerElementId: macroParser('ad_container_id', ''),
      hideObjects: '',
      top: '',
      left: '',
      zIndex: '',
      duration: '',
      wmode: '',
      preferHtml5Artwork: '' == 'true',
      adSenseKeywords: '',
      adSenseLatitude: '',
      adSenseLongitude: '',
      publisherSideFilePath: publisherSideFilePath,
      runtimeMetaData: runtimeMetaData,
      lidarEnabled: false,
      expansionMode: '',
      renderFloatInplace: ''.toLowerCase() == 'true',
      tryToWriteHtmlInline: ''.toLowerCase() == 'true'
    }
  };

  var staticResourceMediaServer = location.protocol == 'https:' ?
       'https://s0.2mdn.net' :
       'http://s0.2mdn.net';

  var creativeMediaServer = location.protocol == 'https:' ?
       'https://s0.2mdn.net' :
       'http://s0.2mdn.net';

  var backupImageUrl = '/ads/richmedia/studio/pv2/31397250/20140516082847347/MSN_FlashBanner_AS3_Collapsed_970x31_backup.jpg';
  if (!/^https?:/.test(backupImageUrl)) {
    backupImageUrl = creativeMediaServer + backupImageUrl;
  }
  var backupImage = {
    exitUrl: 'http://wrapper.g.msn.com/GRedirect.aspx?g.msn.com/2AD000EJ/120000000000191760.1?!&&PID=12048056&UIT=G&TargetID=56063534&N=439354145&PG=UK9SV1&ASID=e0567c73b7b849cc98cf59e5f818a761&ANID=&MUID=3B046F88F0DF64FA24E469C0F4DF664C&destination=http://ad-emea.doubleclick.net/activity;src%3D2567310%3Bmet%3D1%3Bv%3D1%3Bpid%3D108944397%3Baid%3D282155287%3Bko%3D0%3Bcid%3D58179749%3Brid%3D58068862%3Brv%3D1%3Bcs%3Dd%3Beid1%3D1852456%3Becn1%3D1%3Betm1%3D0%3B_dc_redir%3Durl%3fhttp://ad-emea.doubleclick.net/click%3Bh%3Dv8/3f5d/17/ec/%2a/v%3B282155287%3B0-0%3B0%3B108944397%3B43183-970/31%3B58179749/58068862/1%3B%3B%7Esscs%3D%3fhttp://www.kia.co.uk/new-cars/range/compact-cars/soul/view-ibrochure.aspx',
    target: '_blank',
    imageUrl: backupImageUrl,
    width: '970',
    height: '31',
    backupDisplayActivityUrl: [
      adServerData.eventReportingUrl,
      '&timestamp=', (+new Date), ';',
      'eid1=9;ecn1=1;etm1=0;'].join(''),
    thirdPartyBackupImpressionUrl: ''
  };

  var versionPrefix = DEBUG ? 'db_' : '';
  var templateVersion = '200_40';
  var renderingScriptPath = '/879366';
  var rendererDisplayType = '';
  rendererDisplayType += 'flash_';
  var rendererFormat = 'expanding';
  var rendererName = rendererDisplayType + rendererFormat;
  var renderingLibrary = renderingScriptPath + '/' + rendererName + '_rendering_lib_' +
      versionPrefix + templateVersion + '.js';
  // Adserver has a logic to detect media files and prepend host name.
  if (!/^https?:/.test(renderingLibrary)) {
    renderingLibrary = staticResourceMediaServer + renderingLibrary;
  }

  var adCreativeDefinitions = {};

  var creativeId = '1401203825586';
  var adId = adCreativeDefinitions[adServerData.adId] ? adServerData.adId : 0;
  // The unique creative is identified by combination of creative id and ad id.
  // When the same creative(same creative id and same ad id) is served on the page more
  // than once then they will share the creative definition yet there will be
  // multiple instances of 'adResponses'.s
  var creativeKey = [creativeId, adId].join('_');
  var creativeDef = adCreativeDefinitions[adServerData.adId] ?
      adCreativeDefinitions[adServerData.adId] :
      'http://s0.2mdn.net/2567310/plcr_2920992_0_1401203825548.js';
  if(!/^https?:/.test(creativeDef) && creativeDef.substring(0, 2) != '//') {
    creativeDef = creativeMediaServer + creativeDef;
  }
  studioObjects['creativeCount'] = studioObjects['creativeCount'] || 0;
  var creativeDto = {
    id: creativeId,
    uniqueId: creativeId + '_' + studioObjects['creativeCount']++,
    templateVersion: templateVersion,
    adServerData: adServerData,
    isPreviewEnvironment: '%PreviewMode' == 'true',
    hasFlashAsset: true,
    hasHtmlAsset: false,
    requiresCss3Animations: false,
    flashVersion: '9',
    httpsMediaServer: 'https://s0.2mdn.net',
    httpMediaServer: 'http://s0.2mdn.net',
    renderingScriptPath: renderingScriptPath,
    renderingLibrary: renderingLibrary,
    rendererName: rendererName,
    creativeDefinitionUrl: creativeDef,
    creativeKey: creativeKey,
    thirdPartyImpressionUrls: [''],
    thirdPartyArtworkImpressionUrl: '',
    breakoutToTop: false,
    dimensions: {
      width: '970px',
      height: 'auto'
    },
    backupImage: backupImage,
    csiStart: csiStart,
    csiAdRespTime: csiStart - (parseFloat('') || 0),
    csiEvents: {},
    hasModernizrFeatureChecks: false,
    html5FeatureChecks: [
    ],
    hasSwiffyHtmlAsset: false
  };

  var inGdnIframe = window['IN_ADSENSE_IFRAME'] || false;
  var inYahooSecureIframe = window.Y && Y.SandBox && Y.SandBox.vendor;
  var inWinLiveIframe = false;
  try {
    inWinLiveIframe = !!window.$WLXRmAd;
  } catch(e) {}
  var inSafeFrame = window.$sf && window.$sf.ext;
  var isMsnAjaxIframe = (typeof(inDapMgrIf) != 'undefined' && inDapMgrIf);
  var breakoutIframe = ''.toLowerCase();
  var shouldBreakout = (((true ||
                          false) &&
                         !inGdnIframe &&
                         !inYahooSecureIframe &&
                         !inSafeFrame &&
                         !inWinLiveIframe) ||
                        (false && breakoutIframe == 'true')) &&
                       self != top &&
                       !creativeDto.isPreviewEnvironment &&
                       breakoutIframe != 'false';

  if (adServerData.tag.adContainerElementId == '' &&
      (false || true ||
         adServerData.tag.renderFloatInplace)) {
    var containerId = ['creative', creativeDto.uniqueId].join('_');
    var divHtml = ['<div id="', containerId, '"></div>'].join('');
    document.write(divHtml);
    adServerData.tag.adContainerElementId = containerId;
    adServerData.generatedAdSlot = true;
  }
  var creatives = studioObjects['creatives'] = studioObjects['creatives'] || {};
  var creative = creatives[creativeKey] = creatives[creativeKey] || {};
  var adResponses = creative['adResponses'] = creative['adResponses'] || [];
  creative['shouldBreakout'] = creative['shouldBreakout'] || shouldBreakout;
  var iframeBusterLibrary = renderingScriptPath + '/iframe_buster_' +
      versionPrefix + templateVersion + '.js';
  if(!/^https?:/.test(iframeBusterLibrary)) {
    iframeBusterLibrary = staticResourceMediaServer + iframeBusterLibrary;
  }
  var loadedLibraries = studioObjects['loadedLibraries'] = studioObjects['loadedLibraries'] || {};
  var versionedLibrary = loadedLibraries[templateVersion] = loadedLibraries[templateVersion] || {};
  var typedLibrary = versionedLibrary[rendererName] = versionedLibrary[rendererName] || {};
  adResponses.push({
    creativeDto: creativeDto
  });
  if (shouldBreakout) {
    if (versionedLibrary['breakout']) {
      versionedLibrary['breakout']();
    } else if (!versionedLibrary['breakoutLoading']) {
      versionedLibrary['breakoutLoading'] = true;
      document.write('<scr' + 'ipt type="text/javascript" src="' + iframeBusterLibrary + '" async="async"></scr' + 'ipt>');
    }
  } else if (typedLibrary['bootstrap'] && creative['creativeDefinition']) {
    typedLibrary['bootstrap']();
  } else {
    if (!creative['definitionLoading']) {
      creative['definitionLoading'] = true;
      creativeDto.csiEvents['pb'] = (+new Date);
      document.write('<scr' + 'ipt type="text/javascript" src="' + creativeDto.creativeDefinitionUrl + '"' + (adServerData.tag.tryToWriteHtmlInline ? '' : ' async="async"') + '></scr' + 'ipt>');
    }
    if (!typedLibrary['loading']) {
      typedLibrary['loading'] = true;
      creativeDto.csiEvents['gb'] = (+new Date);
      document.write('<scr' + 'ipt type="text/javascript" src="' + renderingLibrary + '"' + (adServerData.tag.tryToWriteHtmlInline ? '' : ' async="async"') + '></scr' + 'ipt>');
    }
  }
  if (isMsnAjaxIframe) {
    window.setTimeout("document.close();", 1000);
  }
})();

document.write('\n<noscript>\n  <a target=\"_blank\" href=\"http://wrapper.g.msn.com/GRedirect.aspx?g.msn.com/2AD000EJ/120000000000191760.1?!&&PID=12048056&UIT=G&TargetID=56063534&N=439354145&PG=UK9SV1&ASID=e0567c73b7b849cc98cf59e5f818a761&ANID=&MUID=3B046F88F0DF64FA24E469C0F4DF664C&destination=http://ad-emea.doubleclick.net/activity;src%3D2567310%3Bmet%3D1%3Bv%3D1%3Bpid%3D108944397%3Baid%3D282155287%3Bko%3D0%3Bcid%3D58179749%3Brid%3D58068862%3Brv%3D1%3Bcs%3Dd%3Beid1%3D1852456%3Becn1%3D1%3Betm1%3D0%3B_dc_redir%3Durl%3fhttp://ad-emea.doubleclick.net/click%3Bh%3Dv8/3f5d/17/ec/%2a/v%3B282155287%3B0-0%3B0%3B108944397%3B43183-970/31%3B58179749/58068862/1%3B%3B%7Esscs%3D%3fhttp://www.kia.co.uk/new-cars/range/compact-cars/soul/view-ibrochure.aspx\">\n    <img border=\"0\" alt=\"\" src=\"//s0.2mdn.net/ads/richmedia/studio/pv2/31397250/20140516082847347/MSN_FlashBanner_AS3_Collapsed_970x31_backup.jpg\"\n        width=\"970\" height=\"31\" />\n  </a>\n  <img width=\"0px\" height=\"0px\" style=\"visibility:hidden\" border=\"0\" alt=\"\"\n       src=\"http://ad-emea.doubleclick.net/activity;src=2567310;met=1;v=1;pid=108944397;aid=282155287;ko=0;cid=58179749;rid=58068862;rv=1;&timestamp=2159714;eid1=9;ecn1=1;etm1=0;\" />\n  <img width=\"0px\" height=\"0px\" style=\"visibility:hidden\" border=\"0\" alt=\"\"\n      src=\"\" />\n  <img width=\"0px\" height=\"0px\" style=\"visibility:hidden\" border=\"0\" alt=\"\"\n      src=\"\" />\n</noscript>\n');
