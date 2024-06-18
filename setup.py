from setuptools import setup, find_packages

setup(
    name='mypackage',  # 패키지 이름
    version='1.0.0',   # 패키지 버전
    packages=find_packages(),  # 패키지를 자동으로 찾아 포함
    install_requires=[
          # 패키지의 의존성 지정
    ],
    entry_points={
        # 실행 가능한 스크립트 등록
    },
    author='ejbang1',  # 패키지 저자
    author_email='ejbang1@seegene.com',  # 저자 이메일
    description='Description of your package',  # 패키지 설명
    # long_description=open('README.md').read(),  # README 파일을 통한 자세한 설명
    # long_description_content_type='text/markdown',  # README 파일의 형식
    
)