import streamlit as st
import streamlit.components.v1 as components

def main():
    """
    Streamlit 앱의 메인 함수입니다.
    지정된 경로의 HTML 파일을 읽어와서 Streamlit 페이지에 표시합니다.
    """

    # 웹페이지의 제목을 설정합니다.
    st.set_page_config(
        page_title="오디오북 감정 분석 연구 계획서",
        layout="wide",
    )

    # HTML 파일의 경로를 설정합니다.
    # 사용자의 요청에 따라 'htmls' 폴더 내의 'index.html'을 지정합니다.
    html_file_path = "htmls/index.html"

    # HTML 파일을 읽어와서 앱에 표시합니다.
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # st.components.v1.html() 함수를 사용하여 HTML을 렌더링합니다.
        # width와 height를 '100%'로 설정하여 컨테이너에 맞게 크기를 조절합니다.
        components.html(html_content, width=None, height=1000, scrolling=True)

    except FileNotFoundError:
        st.error(f"HTML 파일을 찾을 수 없습니다: '{html_file_path}'")
        st.info("HTML 파일이 'htmls' 폴더 안에 있는지 확인하고 파일명을 다시 확인해주세요.")
    except Exception as e:
        st.error(f"파일을 읽는 도중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
