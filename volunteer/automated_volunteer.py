import pyautogui
import time
import os
import zipfile
import os
import pyautogui
import pyperclip
import keyboard

##해당 파일에 대한 설명.
##해당 파일은 월드비전 번역봉사 날먹을하기 위한 프로그램입니다.
##전제조건은 다음과 같습니다. 해상도 2560 1440, 크롬, 100퍼센트 확장된 상태.
# 왼쪽 절반은 번역하기 버튼이 보이는 상태의 월드비전 사이트, 오른쪽은 챗지피티이니다.
#크롬 확장자 중 pdf to jpg 라는 확장자가 추가되어있어야하고, 퍼즐모양(확장자아이콘) 옆에 등록되어있어야합니다.
#바탕화면에 temp라는 폴더가 존재해햐합니다.
#그이상 자세하게는 지금 잠와서 딱히 생각안나서 안적겠습니다. 알잘딱깔센하셈

##한통당 번역 자동화 시간 1분 30초 + 수동체크 및 수정 시간 30초 >> 한통당 2분이 목표입니다.


#추가되어야 하는 기능: 1. 언제든 종료할수있는 핫키 설정.
# gpt 메뉴얼 보강하기, 


def main():
    # # "번역편지 추가" 클릭
    # pyautogui.click(843, 571)
    # time.sleep(0.5)
    # # "확인" 버튼 클릭
    # pyautogui.hotkey('enter')
    # time.sleep(0.5)
    # # "확인" 버튼 한번 더 클릭
    # pyautogui.hotkey('enter')
    # time.sleep(0.5)  # 새 창이 열릴 때까지 대기

    #"번역하기 버튼" 클릭
    pyautogui.click(1151,724)
    time.sleep(0.5)
        
    # 새 번역편지 창을 화면 왼쪽 절반에 배치>> 이경우 오류발생하는경우있음
    pyautogui.hotkey('winleft', 'left')
    time.sleep(0.5)
    
    # 필요한 정보 크롤링 (추가 구현 필요)>>일단 패스
    # OCR이나 페이지 소스 접근이 필요할 수 있습니다.
    
    # 굿레터 추천점수 3점 주기
    pyautogui.click(321, 477)
    time.sleep(0.5)
    
    # 편지 PDF 파일 다운로드
    pyautogui.click(1100,600)
    time.sleep(2)  # 파일 탐색기 창이 열릴 때까지 대기
    
    # 파일을 바탕화면에 저장
    pyautogui.click(55,277)
    time.sleep(0.5)
    pyautogui.click(308,749)
    pyautogui.typewrite('asdf', interval=0.1)
    time.sleep(0.5)
    pyautogui.click(1102,861)
    time.sleep(0.5)

    # jpg로 변환
    #오른쪽 화면에서 퍼즐모양 아이콘 옆의 pdf to jpg 아이콘 클릭
    #이거굳이 이렇게해야하나? 일단주석처리해봄 비교대조 후 필요성있으면 다시 코드로 복귀시킬 것. pyautogui.moveTo(2371, 66, duration=0.5)  # 마우스를 해당 위치로 0.5초 동안 이동
    time.sleep(0.5)
    pyautogui.click(2371,66)
    time.sleep(0.5)

    # pc에서 버튼 클릭
    pyautogui.click(1427, 525)
    time.sleep(1)
    # 바탕화면 클릭
    pyautogui.click(1353, 273)
    time.sleep(0.5)
    # 파일이름 입력란 클릭
    pyautogui.click(1605, 826)
    time.sleep(0.5)
    # asdf 입력
    pyautogui.typewrite('asdf', interval=0.1)
    time.sleep(0.5)
    # enter 입력
    pyautogui.press('enter')
    time.sleep(0.5)
    # 업로드 및 변환 클릭
    pyautogui.click(1483, 853)
    # 15초 기다린 후 >> 이거 시간 줄이면 안됨.
    time.sleep(10)
    # 컴퓨터로 다운로드 클릭
    pyautogui.click(1461, 1070)
    time.sleep(2)
    # pdf to jpg 창 닫기
    pyautogui.click(1773, 21)

    # pdf 삭제
    # 삭제할 파일 경로
    file_path = r'C:\Users\leemi\OneDrive\바탕 화면\asdf.pdf'

    # 파일 삭제
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"파일 {file_path}가 삭제되었습니다.")
    else:
        print(f"파일 {file_path}를 찾을 수 없습니다.")

    # zip 압축해제
    # 경로 설정
    zip_file_path = r'C:\Users\leemi\Downloads\asdf.zip'
    desktop_path = r'C:\Users\leemi\OneDrive\바탕 화면\temp'  # 바탕화면의 temp 폴더 경로
    extract_folder = desktop_path  # 압축을 풀 폴더

    # 압축 해제
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"압축이 {extract_folder}에 해제되었습니다.")

    # 압축전 gif 폴더 삭제
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)
        print(f"파일 {zip_file_path}가 삭제되었습니다.")

    # ChatGPT에 PDF 첨부
    #파일아이콘 클릭
    pyautogui.click(1663, 1317)
    time.sleep(0.5)
    #컴퓨터에서 업로드 클릭
    pyautogui.click(1731, 1263)
    time.sleep(1)
    #경로 검색창 클릭
    pyautogui.click(1692, 56)
    time.sleep(0.5)
    # 클립보드에 경로 복사
    pyperclip.copy(r'C:\Users\leemi\OneDrive\바탕 화면\temp')
    # 붙여넣기
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(1870, 291)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(2495, 1330)
    #바탕화면/temp 폴더의 모든 파일 삭제
        # temp 폴더 경로
    temp_folder_path = r"C:\Users\leemi\OneDrive\바탕 화면\temp"
        # 폴더 내 파일 목록 가져오기
    files = os.listdir(temp_folder_path)
        # 각 파일 삭제
    for file in files:
        file_path = os.path.join(temp_folder_path, file)
            # 파일이 존재하고 파일이면 삭제
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"삭제되었습니다: {file_path}")
        else:
            print(f"파일이 없습니다: {file_path} is not a file")
    #(수동) 챗지피티와의 대화를 통해 보강할것>>핫키누르면 재개
    
    # 재개 대기
    print("f9키를 눌러 재개함. 종료하려면 컨트롤씨누르셈")
    # 'f9' 키가 눌릴 때까지 대기
    keyboard.wait('f9')
    time.sleep(0.5)
    # 'f9' 키가 눌리면 바로 스크립트 실행
    print("스크립트 재개됩니다.")
    time.sleep(0.5)

    # 챗지피티 복사후 붙여넣기
        #아래로가는버튼누르기
    pyautogui.click(2084, 1240)
    time.sleep(0.5)
        #복사버튼 누르기
    pyautogui.click(1744, 1180)
    time.sleep(0.5)
        #번역내용 영역 클릭하기
    pyautogui.click(278, 1313)
        #뒤에 공백 지우기
    pyautogui.hotkey('Delete')
    time.sleep(0.1)
    pyautogui.hotkey('Delete')
    time.sleep(0.1)
    pyautogui.hotkey('Delete')
    time.sleep(0.1)
    pyautogui.hotkey('Delete')
    time.sleep(0.1)
    pyautogui.hotkey('Delete')
    time.sleep(0.1)
    pyautogui.hotkey('Delete')
    time.sleep(0.1)
    pyautogui.hotkey('Delete')
    time.sleep(0.1)
    pyautogui.hotkey('Delete')
    time.sleep(0.1)
        #챗지피티 내용 붙여넣기
    pyautogui.hotkey("ctrl", "v")
    #번역완료 버튼 누르기
    # 재개 대기
    print("f9키를 눌러 재개함. 종료하려면 컨트롤씨누르셈")
    # 'f9' 키가 눌릴 때까지 대기
    keyboard.wait('f9')
    time.sleep(0.5)
    # 'f9' 키가 눌리면 바로 스크립트 실행
    print("스크립트 재개됩니다.")   
    #화면 공백 클릭(스크롤 영역 지정용)
    pyautogui.click(859, 151)
    time.sleep(0.3)
    #왼쪽 창 아래로 내리기
    pyautogui.hotkey('End')
    time.sleep(1)
    #번역완료 클릭하기
    pyautogui.click(1142, 1323)
    time.sleep(0.5)
    #확인누르기
    pyautogui.hotkey('Enter')
    time.sleep(0.5)
    #확인누르기
    pyautogui.hotkey('Enter')
    print("자동화가 완료되었습니다.")
    


while True:
    print("시작하려면 f9누르셈")
    keyboard.wait('f9')
    print("시작합니다.")
    main()