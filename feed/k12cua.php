<?php

function sky_curl_get_file_contents( $url ){
	$c = curl_init();
	curl_setopt( $c, CURLOPT_RETURNTRANSFER, 1 );
	curl_setopt( $c, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/74.0');
	curl_setopt( $c, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt( $c, CURLOPT_VERBOSE, true);
	curl_setopt( $c, CURLOPT_RETURNTRANSFER, true);
	curl_setopt( $c, CURLOPT_URL, $url );
	$contents = curl_exec( $c );
	curl_close( $c );
	if( $contents ) :
		return $contents;
	else:
		return false;
	endif;
}
$url = 'https://mass.mako.co.il/ClicksStatistics/entitlementsServicesV2.jsp?et=ngt&lp=/direct/hls/live/2033791/k12/index.m3u8?as=1&rv=AKAMAI';

$contents = sky_curl_get_file_contents($url);

$json = json_decode($contents, true);

$link = 'https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12/index.m3u8?'.$json['tickets'][0]['ticket'];

header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: '.$link);
exit();
?>