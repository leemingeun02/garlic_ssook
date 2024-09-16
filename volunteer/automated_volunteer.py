import pyautogui
import time
import os
import zipfile
import pyperclip
import keyboard
import glob
import cv2

import numpy as np
from tkinter import Tk, Label
import threading
import sys

# 전역 종료 이벤트
exit_event = threading.Event()

def show_popup(message, duration=3000):
    """
    지정된 메시지를 화면 중앙에 3초간 표시하는 팝업 창을 생성합니다.
    이 함수는 비차단 방식으로 동작하여 메인 스크립트의 실행을 방해하지 않습니다.
    
    :param message: 표시할 메시지 문자열
    :param duration: 메시지를 표시할 시간 (밀리초 단위, 기본값 3000ms)
    """
    def popup():
        root = Tk()
        root.overrideredirect(True)  # 창 장식 제거
        root.attributes("-topmost", True)  # 항상 최상위에 표시
        root.attributes("-alpha", 0.9)  # 창 투명도 설정 (0.0 ~ 1.0)

        # 메시지 라벨 생성
        label = Label(root, text=message, bg='yellow', fg='black', font=('Arial', 14), padx=20, pady=10, wraplength=600, justify='center')
        label.pack()

        # 화면 크기 가져오기
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # 팝업 창 크기 설정 (동적으로 크기 조절)
        root.update_idletasks()  # 라벨 크기 계산을 위해 업데이트
        window_width = root.winfo_width()
        window_height = root.winfo_height()

        # 팝업 창 위치 설정 (화면 중앙)
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 지정된 시간 후 창 닫기
        root.after(duration, root.destroy)
        root.mainloop()

    # 별도의 스레드에서 팝업 실행
    threading.Thread(target=popup, daemon=True).start()

def listen_for_escape():
    """
    Esc 키를 누르면 스크립트를 종료합니다.
    """
    keyboard.wait('esc')
    show_popup("Esc 키가 눌렸습니다. 스크립트를 종료합니다.")
    exit_event.set()

def main():
    '''
    번역편지 추가.
    기존에 편지가 있던 없던 상관없이 수행하면 됩니다.
    '''
    # 스크립트 실행 중 종료 요청이 있는지 확인
    if exit_event.is_set():
        return

    pyautogui.click(865, 570)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)

    if exit_event.is_set():
        return

    # "번역하기" 버튼 클릭
    pyautogui.click(1151, 724)
    time.sleep(0.5)
        
    # 새 번역편지 창을 화면 왼쪽 절반에 배치
    pyautogui.hotkey('winleft', 'left')
    time.sleep(0.5)
    
    
    # 굿레터 추천점수 3점 주기
    pyautogui.click(321, 477)
    time.sleep(0.5)
    
    if exit_event.is_set():
        return

    # 편지 PDF 파일 다운로드
    pyautogui.click(1100, 600)
    time.sleep(2)  # 파일 탐색기 창이 열릴 때까지 대기
        
    # 바탕화면 클릭
    pyautogui.click(55, 277)
    time.sleep(0.5)
    # 이름 입력란 클릭
    pyautogui.click(308, 749)
    pyautogui.typewrite('asdf', interval=0.1)
    time.sleep(0.5)
    # 저장 버튼 클릭
    pyautogui.click(1102, 861)
    time.sleep(0.5)

    if exit_event.is_set():
        return

    # JPG로 변환
    # 오른쪽 화면에서 PDF to JPG 아이콘 클릭
    pyautogui.click(2371, 66)
    time.sleep(1)

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
    time.sleep(8)
    # 컴퓨터로 다운로드 클릭
    pyautogui.click(1461, 1070)
    time.sleep(3)

    if exit_event.is_set():
        return

    # PDF to JPG 창 닫기
    pyautogui.click(1773, 21)

    # pdf 삭제
    # 삭제할 파일 경로
    file_path = r'C:\Users\leemi\OneDrive\바탕 화면\asdf.pdf'

    # 파일 삭제
    if os.path.exists(file_path):
        os.remove(file_path)
        show_popup(f"파일 {file_path}가 삭제되었습니다.")
    else:
        show_popup(f"파일 {file_path}를 찾을 수 없습니다.")

    if exit_event.is_set():
        return

    # 다운로드 폴더에서 가장 최근에 생성된 ZIP 파일 찾기
    downloads_folder = r'C:\Users\leemi\Downloads'
    list_of_files = glob.glob(os.path.join(downloads_folder, '*.zip'))
    if not list_of_files:
        show_popup("다운로드 폴더에 ZIP 파일이 없습니다.")
        return
    else:
        zip_file_path = max(list_of_files, key=os.path.getctime)
    show_popup(f"다운로드된 ZIP 파일: {zip_file_path}")

    if exit_event.is_set():
        return

    # 압축 해제 폴더 설정
    desktop_path = r'C:\Users\leemi\OneDrive\바탕 화면\temp'
    extract_folder = desktop_path

    # 압축 해제
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    show_popup(f"압축이 {extract_folder}에 해제되었습니다.")

    # 압축 파일 삭제
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)
        show_popup(f"파일 {zip_file_path}가 삭제되었습니다.")

    if exit_event.is_set():
        return

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
            show_popup(f"삭제되었습니다: {file_path}")
        else:
            show_popup(f"파일이 아닙니다: {file_path}")

    if exit_event.is_set():
        return

    # (수동) ChatGPT와의 대화를 통해 보강할 것 >> 핫키 누르면 재개

    # 이미지 인식(비활성화된 제출버튼이 나타나면 재개)

    # 해당 버튼으로부터 마우스 치우기(아무데나로)
    pyautogui.moveTo(2050, 745)

    # 이미지 경로 수정
    image_path = r"C:\garlic_ssook\volunteer\submit_button.png"

    time.sleep(10)

    # 타임아웃 설정 (예: 30초)
    timeout = 30  # 타임아웃 시간 (초)
    start_time = time.time()  # 타이머 시작

    # 무한 루프 시작, 이미지를 찾을 때까지 계속 시도
    while True:
        if exit_event.is_set():
            return

        # 템플릿 이미지 로드 및 확인
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            show_popup(f"이미지를 로드할 수 없습니다: {image_path}")
            return

        # 스크린샷 캡처 및 그레이스케일 변환
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        # 템플릿 매칭
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # 매칭된 좌표와 그 강도 찾기
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 매칭된 이미지가 있으면 반복문을 탈출
        if max_val > 0.95:  # 매칭 강도 설정
            show_popup(f"이미지를 찾았습니다! 좌표: {max_loc}")
            break

        # 타임아웃 검사
        if (time.time() - start_time) > timeout:
            show_popup("시간이 초과되었습니다. 이미지를 찾지 못했습니다.")
            break

        # 너무 빠른 반복을 방지하기 위해 잠깐 대기
        time.sleep(1)

        # 나머지 스크립트 실행
        if max_val == 0.95:
            show_popup("이미지를 찾았습니다. 이제 나머지 작업을 진행합니다.")
        else:
            show_popup("이미지를 찾지 못했습니다.")

    if exit_event.is_set():
        return

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
    time.sleep(0.5)
    # 번역 내용 영역 클릭
    pyautogui.click(302, 970)
    # 뒤에 공백 지우기
    for _ in range(8):
        pyautogui.hotkey('Delete')
        time.sleep(0.1)

    if exit_event.is_set():
        return

    # ChatGPT 내용 붙여넣기
    pyautogui.hotkey("ctrl", "v")
    # 번역 완료 버튼 누르기
    # 재개 대기
    show_popup("F9 키를 눌러 재개합니다. 종료하려면 Esc 키를 누르세요.", 10000)
    keyboard.wait('f9')
    if exit_event.is_set():
        return
    time.sleep(0.5)
    show_popup("스크립트를 재개합니다.")
    # 화면 공백 클릭(스크롤 영역 지정용)
    pyautogui.click(859, 151)
    time.sleep(0.3)
    # 왼쪽 창 아래로 내리기
    pyautogui.hotkey('End')
    time.sleep(0.5)
    time.sleep(1)
    # 번역 완료 클릭
    pyautogui.click(1142, 1323)
    time.sleep(0.5)
    # 확인 누르기
    pyautogui.hotkey('Enter')
    time.sleep(0.5)
    # 확인 누르기
    pyautogui.hotkey('Enter')
    show_popup("자동화가 완료되었습니다.")

def run_script():
    # Esc 키를 감지하는 스레드 시작
    escape_thread = threading.Thread(target=listen_for_escape, daemon=True)
    escape_thread.start()

    while not exit_event.is_set():
        show_popup("시작하려면 F9 키를 누르세요.")
        keyboard.wait('f9')
        if exit_event.is_set():
            break

        show_popup("시작합니다.")
        main()

if __name__ == "__main__":
    try:
        run_script()
    except KeyboardInterrupt:
        show_popup("스크립트가 키보드 인터럽트로 종료되었습니다.")
        sys.exit()