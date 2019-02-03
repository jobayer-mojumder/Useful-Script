<?php

<<<<<<< HEAD
$configUpload['upload_path'] = 'excel/';						
$configUpload['encrypt_name'] = FALSE;						
$configUpload['allowed_types'] = 'xls|xlsx|csv';

$this->load->library('upload', $configUpload);
if ($this->upload->do_upload('file')){	
	
	$upload_data = $this->upload->data(); 
	$file_name = $upload_data['file_name'];
						//$extension = $upload_data['file_ext'];


=======
$configUpload['upload_path'] = 'excel/';
$configUpload['encrypt_name'] = FALSE;
$configUpload['allowed_types'] = 'xls|xlsx|csv';

$this->load->library('upload', $configUpload);
if ($this->upload->do_upload('file')){

	$upload_data = $this->upload->data();
	$file_name = $upload_data['file_name'];
						//$extension = $upload_data['file_ext'];
>>>>>>> cce62b3495ec100eb3a4f0ffbbbfb632c4ab7689
	try {
		$this->load->library('excel');
		$objPHPExcel = PHPExcel_IOFactory::load('excel/'.$file_name);}
		catch(Exception $e){
			$this->resp->success = FALSE;
			$this->resp->msg = 'Error Uploading file';
			echo json_encode($this->resp);
			exit;
		}

		$allDataInSheet = $objPHPExcel->getActiveSheet()->toArray(null,true,true,true);
		$i=0;
		foreach($allDataInSheet as $importdata){
			if($i==0){
				$i++;
				continue;
			}
			$postdata = array(
				'investor_code' => $importdata['A'],
				'name' => $importdata['B'],
				'account_status' => $importdata['C'],
				'bo_id' => $importdata['D'],
				'account_type' => $importdata['E'],
				'operation_type' => $importdata['F'],
			);
			$insert = $this->portfolio_model->insert_client_info($postdata);
		}
		$this->session->set_flashdata('msg', 'Data are imported successfully..');
		$path = './excel/' .$file_name ;
		unlink($path);
<<<<<<< HEAD
		redirect('portfolio/client');
=======
		redirect('portfolio/client');
>>>>>>> cce62b3495ec100eb3a4f0ffbbbfb632c4ab7689
