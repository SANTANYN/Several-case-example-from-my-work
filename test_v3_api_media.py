import random
import string
from parametrization import Parametrization
import pytest
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import test_data
from test_data import get_random_name
from test_data import rand
from test_data import random_name2
from test_data import us_access_token
from test_data import prod_access_token
import time
import datetime
from test_data import dev_access_token, random_name2
from pytest_testrail_vox_edition.plugin import pytestrail

"""Это переменные для разных стендов, чтобы запустить тесты на необходимом - закоментить лишний стенд"""

'''eu prod'''
# domain = "domain"
# access_token = prod_access_token()
# upload_media_link = "Some Link"
# search_media_link = "Some Link"
# delete_media_link = "Some Link"

'''us prod'''
# domain = "domain"
# access_token = us_access_token()
# upload_media_link = "Some Link"
# search_media_link = "Some Link"
# delete_media_link = "Some Link"

# '''dev'''
domain = "domain"
access_token = dev_access_token()
upload_media_link = "Some Link"
search_media_link = "Some Link"
delete_media_link = "Some Link"


# @pytestrail.case('C126381', "C126566", "C126567")
class TestV3media:

    @Parametrization.parameters("audio_file", "expected_code")
    @Parametrization.case("xslx_file", 'Book(8).xlsx', 4304)
    @Parametrization.case("aac_file", 'aac_audio-file.aac', 4304)
    @Parametrization.case("amr_file", 'amr_audiofile.amr', 617)
    @Parametrization.case("big_audio__file", 'big_audio_file.mp3', 4303)  # 10mb limit
    @Parametrization.case("opus_file", 'opus_audio_file.opus', 4304)
    @Parametrization.case("ogg_file", 'some_ogg_audiofile.ogg', 4304)
    @Parametrization.case("wrong_format", 'vwrongvideo_mpef_file.mpeg', 4304)
    @Parametrization.case("picture", 'cQKGrkbm7yY — копия.jpg', 4304)
    def test_negative_case_for_upload_media(self, audio_file, expected_code):
        payload = {'domain': domain,
                   'access_token': access_token}
        files = [
            ('file', (f'some_audio_from_API_autotest - {audio_file}',
                      open(f'test_files/{audio_file}',
                           'rb'), 'book(8).xlsx'))
        ]
        response = requests.post(upload_media_link, data=payload, files=files)
        print(response.text)
        result_code = response.json()["result"]["code"]
        assert result_code == expected_code

    @Parametrization.parameters('media_id', 'expected_code')
    @Parametrization.case('string and symbols in id','dsfs!@### !', 400)
    @Parametrization.case('only tab in id', '                      ', 400 )
    @Parametrization.case('too big id', '99999999999999999999999999', 400)
    @Parametrization.case('too small id < 1', '0', 400 )
    def test_search_media_negative_case_id(self, media_id, expected_code):
        payload = {'domain': domain,
                   'access_token': access_token,
                   'id': media_id
                   }
        response = requests.post(search_media_link, data=payload)
        print(response.text)
        result_code = response.json()['result']['code']
        assert result_code == expected_code

    @Parametrization.parameters('folder_id', 'expected_code')
    @Parametrization.case('string and symbols in folder_id', 'dsfs!@### !', 400)
    @Parametrization.case('only tab in folder_id', '                      ', 400)
    @Parametrization.case('too big folder_id', '99999999999999999999999999', 400)
    @Parametrization.case('too small folder_id < 1', '0', 400)
    def test_search_media_negative_case_folder_id(self, folder_id, expected_code):
        payload = {'domain': domain,
                   'access_token': access_token,
                   'folder_id': folder_id
                   }
        response = requests.post(search_media_link, data=payload)
        print(response.text)
        result_code = response.json()['result']['code']
        assert result_code == expected_code

    @Parametrization.parameters('delete_id', 'expected_code')
    @Parametrization.case('string and symbols in delete_id', 'dsfs!@### !', 400)
    @Parametrization.case('only tab in delete_id', '                      ', 400)
    @Parametrization.case('too big delete_id', '99999999999999999999999999', 400)
    @Parametrization.case('too small delete_id < 1', '0', 400)
    @Parametrization.case('does not exist delete_id', ' ', 400)
    @Parametrization.case('wrong delete_id', ' 33535', 404)
    @Parametrization.case('massive in delete_id', '[12,13,33] ', 400)
    @Parametrization.case('json in delete_id', '{"error":"Id must be an integer.","code":400}', 400)
    def test_delete_media_nagative_case(self, delete_id, expected_code):
        payload = {'domain': domain,
                   'access_token': access_token,
                   'id': delete_id
                   }
        response = requests.post(delete_media_link, data=payload)
        print(response.text)
        result_code = response.json()['result']['code']
        assert result_code == expected_code
        payload_upload = {'domain': domain,
                          'access_token': access_token}
        files = [
            ('file', (f'some_audio_from_API_autotest',
                      open('test_files/file_42.mp3',
                           'rb'), 'book(8).xlsx'))
        ]
        response = requests.post(upload_media_link, data=payload_upload, files=files)
        print(response.text)
        result_id = response.json()["result"]["id"]
        payload_delete = {'domain': domain,
                          'access_token': access_token,
                          'id': result_id
                        }
        response = requests.post(delete_media_link, data=payload_delete)
        print(response.text)
        assert response.status_code == 200

    def test_positive_add_media_file(self):
            payload = {'domain': domain,
                       'access_token': access_token}
            files = [
                ('file', (f'some_audio_from_API_autotest_{random_name2}',
                          open('test_files/file_42.mp3',
                               'rb'), 'book(8).xlsx'))
            ]
            response = requests.post(upload_media_link, data=payload, files=files)
            print(response.text)
            result_code = response.status_code

            assert result_code == 200


