<?php
public function client_print(){
		if($this->session->userdata('client_id')){
			$this->load->library('Pdf');
			$pdf = $this->pdf->load();

			$id = $this->session->userdata('client_code');
			$data['total_cost'] = $this->clientuser_model->get_totalcost($id);
			$data['market_value'] = $this->clientuser_model->get_marketvalue($id);
			$data['info'] = $this->clientuser_model->get_clientuser_info($id);
			$data['stk'] = $this->clientuser_model->get_clientuser_stk($id);
			$data['ledger'] = $this->clientuser_model->get_clientuser_ledger($id);
			$html = $this->load->view('clientuser/clientuser_print', $data, true);
			$pdf->WriteHTML($html); 
			$output = 'nrbcbsl-'. date('Y_m_d_H_i_s') . '-.pdf';
			$pdf->Output("$output", 'I');
			exit();
		}else{
			redirect('clientuser/login');
		}
	}