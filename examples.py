examples = {
    
    'activities' : [   
        
        { 'activityID': 1, 'title': 'OPME', 'subtitle': 'Finalizar conta', 'sla': 5},
        { 'activityID': 2, 'title': 'Auditoria', 'subtitle': 'Limpar conta', 'sla': 3},
        { 'activityID': 3, 'title': 'Berçario', 'subtitle': 'Organizar prontuário', 'sla': 2},
        { 'activityID': 4, 'title': 'Centro Cirurgico', 'subtitle': 'Organizar prontuário', 'sla': 2}
    ],
    'cards' : [
        {
            'cardID': 1,
            'daysSinceCreated': 20,
            'slaStatus': 'DELAYED',
            'visitID': 1,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 1,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 1,
            'patientID':  1,
            'billID': 1
        }, {
            'cardID': 2,
            'daysSinceCreated': 7,
            'slaStatus': 'DELAYED',
            'visitID': 2,
            'numberOfDocuments': 1,
            'numberOfNotReceivedDocuments': 0,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 2,
            'patientID':  2,
            'billID': 2
        }, {
            'cardID': 3,
            'daysSinceCreated': 6,
            'slaStatus': 'DELAYED',
            'visitID': 3,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 2,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 2,
            'patientID':  3,
            'billID': 3
        }, {
            'cardID': 4,
            'daysSinceCreated': 4,
            'slaStatus': 'WARNING',
            'visitID': 4,
            'numberOfDocuments': 2,
            'numberOfNotReceivedDocuments': 3,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 3,
            'patientID':  4,
            'billID': 4
        }, {
            'cardID': 5,
            'daysSinceCreated': 4,
            'slaStatus': 'WARNING',
            'visitID': 5,
            'numberOfDocuments': 2,
            'numberOfNotReceivedDocuments': 3,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 2,
            'patientID':  5,
            'billID': 5
        }, {
            'cardID': 6,
            'daysSinceCreated': 1,
            'slaStatus': 'OK',
            'visitID': 6,
            'numberOfDocuments': 2,
            'numberOfNotReceivedDocuments': 3,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 4,
            'patientID':  6,
            'billID': 6
        }, {
            'cardID': 7,
            'daysSinceCreated': 1,
            'slaStatus': 'OK',
            'visitID': 7,
            'numberOfDocuments': 5,
            'numberOfNotReceivedDocuments': 0,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 5,
            'patientID':  7,
            'billID': 7
        }, {
            'cardID': 8,
            'daysSinceCreated': 1,
            'slaStatus': 'OK',
            'visitID': 8,
            'numberOfDocuments': 2,
            'numberOfNotReceivedDocuments': 3,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 2,
            'patientID':  8,
            'billID': 8
        }, {
            'cardID': 9,
            'daysSinceCreated': 0,
            'slaStatus': 'OK',
            'visitID': 9,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 5,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 6,
            'patientID': 9,
            'billID': 9
        }, {
            'cardID': 10,
            'daysSinceCreated': 0,
            'slaStatus': 'OK',
            'visitID': 10,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 5,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsuranceID': 2,
            'patientID': 10,
            'billID': 10
        }
    ],
    'healthInsurances' : [
        {'healthInsuranceID': 1, 'name': 'Maxima Seguro'},
        {'healthInsuranceID': 2, 'name': 'Inter Plena'},
        {'healthInsuranceID': 3, 'name': 'Bio Inter'},
        {'healthInsuranceID': 4, 'name': 'Unicorp Plan'},
        {'healthInsuranceID': 5, 'name': 'Saude Plena'},
        {'healthInsuranceID': 6, 'name': 'Maxima Unicorp'}
    ],
    'bills' : [
        {
            'billID': 1,
            'billType': 'HOSPITALAR',
            'totalAmount': 8925.55,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }, {
            'billID': 2,
            'billType': 'HOSPITALAR',
            'totalAmount': 30313.51,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        },
        
        {
            'billID': 3,
            'billType': 'HOSPITALAR',
            'totalAmount': 8580.28,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }, {
            'billID': 4,
            'billType': 'HOSPITALAR',
            'totalAmount': 15097.21,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }, {
            'billID': 5,
            'billType': 'HOSPITALAR',
            'totalAmount': 6507.64,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }, {
            'billID': 6,
            'billType': 'HOSPITALAR',
            'totalAmount': 30814.31,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }, {
            'billID': 7,
            'billType': 'HOSPITALAR',
            'totalAmount': 8526.71,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }, {
            'billID': 8,
            'billType': 'HOSPITALAR',
            'totalAmount': 24276.19,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }, {
            'billID': 9,
            'billType': 'HOSPITALAR',
            'totalAmount': 1728.59,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }, {
            'billID': 10,
            'billType': 'HOSPITALAR',
            'totalAmount': 25335.76,
            'numberOfPendencies': 0,
            'numberOfOpenPendencies': 0
        }
    ],
    'patients' : [
        { 'patientID' :  1, 'name': 'Fernando Leite Serrano'    },
        { 'patientID' :  2, 'name': 'Graziely Scharf Borelli'   },
        { 'patientID' :  3, 'name': 'Darley Otavio Arroyo'      },
        { 'patientID' :  4, 'name': 'Anderson Marquez Azevedo'  },
        { 'patientID' :  5, 'name': 'Alaor Felisberto Tulio'    },
        { 'patientID' :  6, 'name': 'Veronica Martins Vitoria'  },
        { 'patientID' :  7, 'name': 'Ivone Campos Fernanda'     },
        { 'patientID' :  8, 'name': 'Nilson Figueira Carmo'     },
        { 'patientID' :  9, 'name': 'Guilherme Cosseti Mendonca'},
        { 'patientID' : 10, 'name': 'Francisco Chaves Evarista' }
    ]
}

outputs = {
    'cards' : [
        {
            'cardID': 1,
            'daysSinceCreated': 20,
            'slaStatus': 'DELAYED',
            'visitID': 1,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 1,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 1, 'name': 'Maxima Seguro' },
            'patient': { 'patientID' :  1, 'name': 'Fernando Leite Serrano'    },
            'bill' : { 
                'billID': 1,
                'billType': 'HOSPITALAR',
                'totalAmount': 8925.55,
                'numberOfPendencies': 0, 
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 2,
            'daysSinceCreated': 7,
            'slaStatus': 'DELAYED',
            'visitID': 2,
            'numberOfDocuments': 1,
            'numberOfNotReceivedDocuments': 0,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance' : { 'healthInsuranceID': 2, 'name': 'Inter Plena' },
            'patient': { 'patientID' :  2, 'name': 'Graziely Scharf Borelli'   },
            'bill' : {
                'billID': 2,
                'billType': 'HOSPITALAR',
                'totalAmount': 30313.51,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 3,
            'daysSinceCreated': 6,
            'slaStatus': 'DELAYED',
            'visitID': 3,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 2,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance' : { 'healthInsuranceID': 2, 'name': 'Inter Plena' },
            'patient': { 'patientID' :  3, 'name': 'Darley Otavio Arroyo'      },
            'bill' : {
                'billID': 3,
                'billType': 'HOSPITALAR',
                'totalAmount': 8580.28,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 4,
            'daysSinceCreated': 4,
            'slaStatus': 'WARNING',
            'visitID': 4,
            'numberOfDocuments': 2,
            'numberOfNotReceivedDocuments': 3,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 3, 'name': 'Bio Inter' },
            'patient': { 'patientID' :  4, 'name': 'Anderson Marquez Azevedo'  },
            'bill' : {
                'billID': 4,
                'billType': 'HOSPITALAR',
                'totalAmount': 15097.21,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 5,
            'daysSinceCreated': 4,
            'slaStatus': 'WARNING',
            'visitID': 5,
            'numberOfDocuments': 2,
            'numberOfNotReceivedDocuments': 3,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance' : { 'healthInsuranceID': 2, 'name': 'Inter Plena' },
            'patient': { 'patientID' :  5, 'name': 'Alaor Felisberto Tulio'    },
            'bill' : {
                'billID': 5,
                'billType': 'HOSPITALAR',
                'totalAmount': 6507.64,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 6,
            'daysSinceCreated': 1,
            'slaStatus': 'OK',
            'visitID': 6,
            'numberOfDocuments': 2,
            'numberOfNotReceivedDocuments': 3,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 4, 'name': 'Unicorp Plan' },
            'patient': { 'patientID' :  6, 'name': 'Veronica Martins Vitoria'  },
            'bill' : {
                'billID': 6,
                'billType': 'HOSPITALAR',
                'totalAmount': 30814.31,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 7,
            'daysSinceCreated': 1,
            'slaStatus': 'OK',
            'visitID': 7,
            'numberOfDocuments': 5,
            'numberOfNotReceivedDocuments': 0,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 5, 'name': 'Saude Plena' },
            'patient': { 'patientID' :  7, 'name': 'Ivone Campos Fernanda'     },
            'bill' : {
                'billID': 7,
                'billType': 'HOSPITALAR',
                'totalAmount': 8526.71,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 8,
            'daysSinceCreated': 1,
            'slaStatus': 'OK',
            'visitID': 8,
            'numberOfDocuments': 2,
            'numberOfNotReceivedDocuments': 3,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance' : { 'healthInsuranceID': 2, 'name': 'Inter Plena' },
            'patient': { 'patientID' :  8, 'name': 'Nilson Figueira Carmo'     },
            'bill' : {
                'billID': 8,
                'billType': 'HOSPITALAR',
                'totalAmount': 24276.19,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 9,
            'daysSinceCreated': 0,
            'slaStatus': 'OK',
            'visitID': 9,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 5,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 6, 'name': 'Maxima Unicorp' },
            'patient': { 'patientID' :  9, 'name': 'Guilherme Cosseti Mendonca'},
            'bill' : {
                'billID': 9,
                'billType': 'HOSPITALAR',
                'totalAmount': 1728.59,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }, {
            'cardID': 10,
            'daysSinceCreated': 0,
            'slaStatus': 'OK',
            'visitID': 10,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 5,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance' : { 'healthInsuranceID': 2, 'name': 'Inter Plena' },
            'patient': { 'patientID' : 10, 'name': 'Francisco Chaves Evarista' },
            'bill' : {
                'billID': 10,
                'billType': 'HOSPITALAR',
                'totalAmount': 25335.76,
                'numberOfPendencies': 0,
                'numberOfOpenPendencies': 0
            }
        }
    ]
}
