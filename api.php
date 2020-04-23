<?php

// Setup incoming data
header("Access-Control-Allow-Origin: *");
header('Access-Control-Allow-Methods: POST');
$method = $_SERVER['REQUEST_METHOD'];

// Get incoming data
$data = json_decode(file_get_contents('php://input'));
$headers = apache_request_headers();

// Check de data and put into coronavirus.csv
if($method == "POST" && isset($data) && count($data) == 18 && $headers['PASSWORD'] == "YOURPASSWORDAPI"){
    $csv = fopen('coronavirus.csv', 'a');
    for($i=1;$i<count($data)-1;$i++){
        $line = array($data[$i][0], date('d-m-Y'), $data[$i][2], $data[$i][4]);
        fputcsv($csv, $line);
    }
    fclose($csv);
    return http_response_code(200);
}

return http_response_code(400);

?>