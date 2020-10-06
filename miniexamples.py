examples = {
    
    'activities' : [   
        { 'activityID': 1, 'title': 'OPME', 'subtitle': 'Finalizar conta', 'sla': 5},
        { 'activityID': 2, 'title': 'Auditoria', 'subtitle': 'Limpar conta', 'sla': 3},
        { 'activityID': 3, 'title': 'Berçario', 'subtitle': 'Organizar prontuário', 'sla': 2}
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
        }
    ],
    'healthInsurances' : [
        {'healthInsuranceID': 1, 'name': 'Maxima Seguro'},
        {'healthInsuranceID': 2, 'name': 'Inter Plena'},
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
        }
    ],
    'patients' : [
        { 'patientID' :  1, 'name': 'Fernando Leite Serrano'    },
        { 'patientID' :  2, 'name': 'Graziely Scharf Borelli'   },
        { 'patientID' :  3, 'name': 'Darley Otavio Arroyo'      }
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
        }
    ]
}

test = [
    {
        'input' : {
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
        }
    },
    {
        'input'  : 'Fernando Leite Serrano',
        'output' : [{
            'cardID': 1,
            'daysSinceCreated': 20,
            'slaStatus': 'DELAYED',
            'visitID': 1,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 1,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 1, 'name': 'Maxima Seguro' },
            'patient': { 'patientID' :  1, 'name': 'Fernando Leite Serrano' },
            'bill' : { 
                'billID': 1,
                'billType': 'HOSPITALAR',
                'totalAmount': 8925.55,
                'numberOfPendencies': 0, 
                'numberOfOpenPendencies': 0
            }
        }]
    },
    {
        'input'  : 1,
        'output' : [{
            'cardID': 1,
            'daysSinceCreated': 20,
            'slaStatus': 'DELAYED',
            'visitID': 1,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 1,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 1, 'name': 'Maxima Seguro' },
            'patient': { 'patientID' :  1, 'name': 'Fernando Leite Serrano' },
            'bill' : { 
                'billID': 1,
                'billType': 'HOSPITALAR',
                'totalAmount': 8925.55,
                'numberOfPendencies': 0, 
                'numberOfOpenPendencies': 0
            }
        }]
    },
    {
        'input'  : 1,
        'output' : [{
            'cardID': 1,
            'daysSinceCreated': 20,
            'slaStatus': 'DELAYED',
            'visitID': 1,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 1,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 1, 'name': 'Maxima Seguro' },
            'patient': { 'patientID' :  1, 'name': 'Fernando Leite Serrano' },
            'bill' : { 
                'billID': 1,
                'billType': 'HOSPITALAR',
                'totalAmount': 8925.55,
                'numberOfPendencies': 0, 
                'numberOfOpenPendencies': 0
            }
        }]
    },
    {
        'input'  : 1,
        'output' : [{
            'cardID': 1,
            'daysSinceCreated': 20,
            'slaStatus': 'DELAYED',
            'visitID': 1,
            'numberOfDocuments': 0,
            'numberOfNotReceivedDocuments': 1,
            'numberOfChecklistItem': 0,
            'numberOfDoneChecklistItem': 0,
            'healthInsurance': { 'healthInsuranceID': 1, 'name': 'Maxima Seguro' },
            'patient': { 'patientID' :  1, 'name': 'Fernando Leite Serrano' },
            'bill' : { 
                'billID': 1,
                'billType': 'HOSPITALAR',
                'totalAmount': 8925.55,
                'numberOfPendencies': 0, 
                'numberOfOpenPendencies': 0
            }
        }]
    }
]