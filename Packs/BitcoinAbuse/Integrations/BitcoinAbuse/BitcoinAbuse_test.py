""" Bitcoin Abuse Integration for Cortex XSOAR - Unit Tests file
"""

from BitcoinAbuse import *

SERVER_URL = 'https://www.bitcoinabuse.com/api/'

client = BitcoinAbuseClient(
    api_key='',
    verify=False,
    proxy=False
)

failure_mock_response = {
    'response': 'Description is mandatory',
    'success': False
}

success_mock_response = {
    'response': 'Uploaded address successfuly',
    'success': True
}

failure_report_address_other_type_missing = {
    'address': '12xfas41',
    'abuser': 'blabla@blabla.net',
    'abuse_type': 'other',
    'description': 'this is a description of an abuse done to the api'
}

success_report_address_other_type = {
    'address': '12xfas41',
    'abuser': 'blabla@blabla.net',
    'abuse_type': 'other',
    'abuse_type_other': 'Stole my bitcoins',
    'description': 'this is a description of an abuse done to the api'
}

success_report_address = {
    'address': '12xfas41',
    'abuser': 'blabla@blabla.net',
    'abuse_type': 'darknet market',
    'description': 'this is a description of an abuse done to the api'
}

failure_report_address_unknown_type = {
    'address': '12xfas41',
    'abuser': 'blabla@blabla.net',
    'abuse_type': 'unknown type',
    'abuse_type_other': 'Stole my bitcoins',
    'description': 'this is a description of an abuse done to the api'
}


def test_report_address_command_success(requests_mock):
    requests_mock.post(
        'https://www.bitcoinabuse.com/api/reports/create',
        json=success_mock_response
    )
    assert report_address_command(client,
                                  success_report_address) == 'bitcoin address 12xfas41 by abuser ' \
                                                             'blabla@blabla.net was reported to ' \
                                                             'BitcoinAbuse API'


def test_report_address_command_failure(requests_mock):
    mocker.patch.object(client, 'report_address', return_value=success_mock_response)
    try:
        report_address_command(client, success_report_address)
        raise AssertionError('report address command should fail when not given success response from api')
    except DemistoException as error_msg:
        a = 2


def test_report_address_command_success_type_other(requests_mock):
    requests_mock.post(
        'https://www.bitcoinabuse.com/api/reports/create',
        json=success_mock_response
    )
    assert report_address_command(client,
                                  success_report_address_other_type) == 'bitcoin address 12xfas41 by abuser ' \
                                                                        'blabla@blabla.net was reported to ' \
                                                                        'BitcoinAbuse API'

#
# def test_report_address_command_failure_type_other():
#     try:
#         report_address_command(client, failure_report_address_other_type_missing)
#         raise AssertionError('report address command should fail when type is other and no abuse_type_other was given')
#     except DemistoException as error:
#         assert error.message == 'Bitcoin Abuse: abuse_type_other is mandatory when abuse type is other'
#
#
# def test_report_address_command_failure_unknown_type():
#     try:
#         report_address_command(client, failure_report_address_unknown_type)
#         raise AssertionError('report address command should fail when not given a known type')
#     except DemistoException as error:
#         assert error.message == 'Bitcoin Abuse: invalid type of abuse, please insert a correct abuse type'
