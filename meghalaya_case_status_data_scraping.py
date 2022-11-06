from bs4 import BeautifulSoup
import requests
import json

session = requests.session()
url1 = "https://meghalayahighcourt.nic.in/case-status"
url2 = "https://meghalayahighcourt.nic.in/case-status?ajax_form=1&_wrapper_format=drupal_ajax"
response1 = session.get(url1 , verify = False)
content1 = response1.content
soup1 = BeautifulSoup(content1, "lxml")
# print(soup1)
final_data_result =[]
data_result = {}

Headers1 = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "en-US,en;q=0.5",
        "Connection" : "keep-alive",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Host" : "meghalayahighcourt.nic.in",
        "Origin" : "https://meghalayahighcourt.nic.in",
        "Referer" : "https://meghalayahighcourt.nic.in/case-status",
        "Sec-Fetch-Dest" : "empty",
        "Sec-Fetch-Mode" : "cors",
        "Sec-Fetch-Site" : "same-origin",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "X-Requested-With" : "XMLHttpRequest"
    }
	

payload1 = {}
payload2 = {}
form_build_id = soup1.find("input",{"name":"form_build_id"})["value"]
ajax_page_state = soup1.find("script",{"data-drupal-selector":"drupal-settings-json"}).text.strip()
ajax_data = json.loads(ajax_page_state)
final_ajax_data = ajax_data["ajaxPageState"]
ajax_page_state = final_ajax_data["libraries"]
# print(ajax_page_state)
payload1["qry"] = "case"
payload1["form_build_id"] = form_build_id
payload1["form_id"] = "case_status_form1"
payload1["reg_no"] = ""
payload1["ptyname"] = ""
payload1["advname"] = ""
payload1["_triggering_element_name"] = "qry"
payload1["_drupal_ajax"] = "1"
payload1["ajax_page_state[theme]"] = "meghc"
payload1["ajax_page_state[theme_token]"] = ""
payload1["ajax_page_state[libraries]"] = ajax_page_state
# print(payload1)


response2 = session.post(url2, headers=Headers1 , data=payload1, verify = False)
response_data2 = response2.json()
# print(response_data2)
response_data_position2 = response_data2[0]
# print(response_data_position2)


# form_build_id_new = response_data_position2["new"]
payload2["qry"] = "case"
payload2["form_build_id"] = "form-in9RAniIqd35ije6QtykrUxshKmMFY0Ezc8RDby-h90"#form_build_id_new
payload2["form_id"] = "case_status_form1"
payload2["case_type"] = "Arb.P."
payload2["reg_no"] = "2"
payload2["year"] = "2022"
payload2["ptyname"] = ""
payload2["advname"] = ""
payload2["_triggering_element_name"] = "op"
payload2["_triggering_element_value"] = "Search"
payload2["_drupal_ajax"] = "1"
payload2["ajax_page_state[theme]"] = "meghc"
payload2["ajax_page_state[libraries]"] = "accessibility/accessibility,case_status/case_status,case_status/recaptcha,core/drupal.states,core/drupal.tableresponsive,core/jquery.form,datatables/datatables-default,datatables/datatables-default-fixed-header,datatables/datatables-default-responsive,extlink/drupal.extlink,flexslider/integration,mayo/global-styling,meghc/global-scripts,meghc/global-styling,meghc/responsive-layout,scrollup/scrollup,social_media_links/social_media_links.theme,styleswitcher/dynamic-css,styleswitcher/styleswitcher,superfish/superfish,superfish/superfish_hoverintent,superfish/superfish_smallscreen,superfish/superfish_style_white,superfish/superfish_supersubs,superfish/superfish_supposition,system/base,text_resize/text_resize.resize,views/views.module,vjr_views/vjr_views"
# print(payload2)

response3 = session.post(url2, headers=Headers1 , data=payload2, verify = False)
response_data3 = response3.json()
# print(response_data3)
response_data3_content = response_data3[19]["data"]
# print(response_data3_content)
soup2 = BeautifulSoup(response_data3_content,"html.parser")
# print(soup2)
final_response_data = soup2.find("div",{"id":"cdetails"})#.text.strip()

# print(final_response_data)
final_response_data_value = final_response_data.findAll("tr")[1]
# print(final_response_data_value)
final_data_value = final_response_data_value.find_all("td")
# print(final_data_value)
case_no = final_data_value[0].text.strip()
petitioner = final_data_value[1].text.strip()
respondent = final_data_value[2].text.strip()
status = final_data_value[3].text.strip()

data_result["Case No."] = case_no
data_result["Petitioner"] = petitioner
data_result["Respondent"] = respondent
data_result["status"] = status
# print(data_result)
final_data_result.append(data_result)
print(final_data_result)






