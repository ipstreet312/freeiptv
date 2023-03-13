<?php

function sky_curl_get_file_contents( $url ){
	$c = curl_init();
	curl_setopt( $c, CURLOPT_RETURNTRANSFER, 1 );
	curl_setopt( $c, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/74.0');
	curl_setopt( $c, CURLOPT_URL, $url );
	$contents = curl_exec( $c );
	curl_close( $c );
	if( $contents ) :
		return $contents;
	else:
		return false;
	endif;
}
$url = 'https://services.iol.pt/matrix?userId=';

$contents = sky_curl_get_file_contents($url);

$link = 'https://video-auth7.iol.pt/live_cnn/live_cnn/playlist.m3u8?wmsAuthSign='.$contents;

header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: '.$link);
exit();
?>