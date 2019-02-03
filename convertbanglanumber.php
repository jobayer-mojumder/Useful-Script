<?php
function changeDigitsEtoB( $digits ) {
	$bangla = numfmt_format(numfmt_create( 'bn_BD', NumberFormatter::TYPE_DEFAULT ),$digits); //Bangla locale
	return $bangla;
}
echo changeDigitsEtoB(1234); //output ১২৩৪
