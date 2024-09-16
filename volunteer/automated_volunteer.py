import pyautogui
import time
import os
import zipfile
import pyperclip
import keyboard
import glob
import cv2
import numpy as np

def main():
    # "번역하기" 버튼 클릭
    pyautogui.click(1151, 724)
    time.sleep(0.5)
        
    # 새 번역편지 창을 화면 왼쪽 절반에 배치
    pyautogui.hotkey('winleft', 'left')
    time.sleep(0.5)
    
    # 굿레터 추천점수 3점 주기
    pyautogui.click(321, 477)
    time.sleep(0.5)
    
    # 편지 PDF 파일 다운로드
    pyautogui.click(1100, 600)
    time.sleep(2)  # 파일 탐색기 창이 열릴 때까지 대기
        
    # 파일을 바탕화면에 저장
    pyautogui.click(55, 277)
    time.sleep(0.5)
    pyautogui.click(308, 749)
    pyautogui.typewrite('asdf', interval=0.1)
    time.sleep(0.5)
    pyautogui.click(1102, 861)
    time.sleep(0.5)

    # JPG로 변환
    # 오른쪽 화면에서 PDF to JPG 아이콘 클릭
    time.sleep(0.5)
    pyautogui.click(2371, 66)
    time.sleep(0.5)

    # "PC에서" 버튼 클릭
    pyautogui.click(1427, 525)
    time.sleep(1)
    # 바탕화면 클릭
    pyautogui.click(1353, 273)
    time.sleep(0.5)
    # 파일 이름 입력란 클릭
    pyautogui.click(1605, 826)
    time.sleep(0.5)
    # 'asdf' 입력
    pyautogui.typewrite('asdf', interval=0.1)
    time.sleep(0.5)
    # Enter 입력
    pyautogui.press('enter')
    time.sleep(0.5)
    # 업로드 및 변환 클릭
    pyautogui.click(1483, 853)
    # 10초 기다리기
    time.sleep(10)
    # 컴퓨터로 다운로드 클릭
    pyautogui.click(1461, 1070)
    time.sleep(5)  # 다운로드 시간을 충분히 줍니다.

    # PDF to JPG 창 닫기
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



    # 다운로드 폴더에서 가장 최근에 생성된 ZIP 파일 찾기
    downloads_folder = r'C:\Users\leemi\Downloads'
    list_of_files = glob.glob(os.path.join(downloads_folder, '*.zip'))
    if not list_of_files:
        print("다운로드 폴더에 ZIP 파일이 없습니다.")
        return
    else:
        zip_file_path = max(list_of_files, key=os.path.getctime)
    print(f"다운로드된 ZIP 파일: {zip_file_path}")

    # 압축 해제 폴더 설정
    desktop_path = r'C:\Users\leemi\OneDrive\바탕 화면\temp'
    extract_folder = desktop_path

    # 압축 해제
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"압축이 {extract_folder}에 해제되었습니다.")

    # 압축 파일 삭제
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)
        print(f"파일 {zip_file_path}가 삭제되었습니다.")

    # ChatGPT에 이미지 첨부
    # 파일 아이콘 클릭
    pyautogui.click(1663, 1317)
    time.sleep(0.5)
    # "컴퓨터에서 업로드" 클릭
    pyautogui.click(1731, 1263)
    time.sleep(1)
    # 경로 검색창 클릭
    pyautogui.click(1692, 56)
    time.sleep(0.5)
    # 클립보드에 경로 복사
    pyperclip.copy(r'C:\Users\leemi\OneDrive\바탕 화면\temp')
    # 붙여넣기
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
    # 모든 파일 선택 후 열기
    pyautogui.click(1870, 291)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(2495, 1330)
    # 바탕화면/temp 폴더의 모든 파일 삭제
    temp_folder_path = r"C:\Users\leemi\OneDrive\바탕 화면\temp"
    files = os.listdir(temp_folder_path)
    for file in files:
        file_path = os.path.join(temp_folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"삭제되었습니다: {file_path}")
        else:
            print(f"파일이 없습니다: {file_path}는 파일이 아닙니다.")
    # (수동) ChatGPT와의 대화를 통해 보강할 것 >> 핫키 누르면 재개



    #이미지 인식(비활성화된 제출버튼이 나타나면 재개)

    #해당 버튼으로부터 마우스 치우기(아무데나로)
    pyautogui.moveTo(2050, 745)

    
    # 146번째 줄부터 수정된 부분
    # 이미지 경로 수정
    image_path = r"C:\garlic_ssook\volunteer\submit_button.png"

    time.sleep(10)

    # 타임아웃 설정 (예: 30초)
    timeout = 30  # 타임아웃 시간 (초)
    start_time = time.time()  # 타이머 시작

    # 무한 루프 시작, 이미지를 찾을 때까지 계속 시도
    while True:
        # 템플릿 이미지 로드 및 확인
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"이미지를 로드할 수 없습니다: {image_path}")
            return

        # 스크린샷 캡처 및 그레이스케일 변환
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        # 템플릿 매칭
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # 매칭된 좌표와 그 강도 찾기
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 매칭된 이미지가 있으면 반복문을 탈출
        if max_val >0.95:  # 매칭 강도 설정
            print(f"이미지를 찾았습니다! 좌표: {max_loc}")
            break

        # 타임아웃 검사
        if (time.time() - start_time) > timeout:
            print("시간이 초과되었습니다. 이미지를 찾지 못했습니다.")
            break

        # 너무 빠른 반복을 방지하기 위해 잠깐 대기
        time.sleep(1)


        # 나머지 스크립트 실행
        if max_val == 0.95:
            print("이미지를 찾았습니다. 이제 나머지 작업을 진행합니다.")
        else:
            print("이미지를 찾지 못했습니다.")





    # ChatGPT 답변 복사 후 붙여넣기
    # 아래로 스크롤 버튼 클릭
    pyautogui.click(2084, 1240)
    time.sleep(0.5)
    # 복사 버튼 클릭
    pyautogui.click(1744, 1180)
    time.sleep(0.5)
    # 화면 공백 클릭(스크롤 영역 지정용)
    pyautogui.click(859, 151)
    time.sleep(0.3)
    # 왼쪽 창 아래로 내리기
    pyautogui.hotkey('End')
    pyautogui.sleep(0.5)
    # 번역 내용 영역 클릭
    pyautogui.click(302, 970)
    # 뒤에 공백 지우기
    for _ in range(8):
        pyautogui.hotkey('Delete')
        time.sleep(0.1)
    # ChatGPT 내용 붙여넣기
    pyautogui.hotkey("ctrl", "v")
    # 번역 완료 버튼 누르기
    # 재개 대기
    print("F9 키를 눌러 재개합니다. 종료하려면 Ctrl+C를 누르세요.")
    keyboard.wait('f9')
    time.sleep(0.5)
    print("스크립트를 재개합니다.")
    # 화면 공백 클릭(스크롤 영역 지정용)
    pyautogui.click(859, 151)
    time.sleep(0.3)
    # 왼쪽 창 아래로 내리기
    pyautogui.hotkey('End')
    pyautogui.sleep(0.5)
    time.sleep(1)
    # 번역 완료 클릭
    pyautogui.click(1142, 1323)
    time.sleep(0.5)
    # 확인 누르기
    pyautogui.hotkey('Enter')
    time.sleep(0.5)
    # 확인 누르기
    pyautogui.hotkey('Enter')
    print("자동화가 완료되었습니다.")

while True:
    print("시작하려면 F9 키를 누르세요.")
    keyboard.wait('f9')
    print("시작합니다.")
    main()