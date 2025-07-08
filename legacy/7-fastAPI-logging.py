import logging

'''

#######################################################################
## [Level]

## 레벨                         설명                                         출력조건
-------------------------------------------------------------------------------------------------
   DEBUG                상세한 내부 상태 출력(개발 단계)             level=logging.DEBUG일 때만
   INFO                 일반적인 정보 메시지                         INFO 이상 설정 시 출력
   WARNING              경고 사항                                    WARNING 이상
   ERROR                에러                                         ERRPR 이상
   CRITICAL             치명적 오류                                  항상 출력


## [로그 레벨 순서] 낮음 -> 높음
## DEBUG < INFO < WARNING <ERROR < CRITICAL
#################################################################################################


'''

## 1.로깅 기본 설정
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=logging.CRITICAL)
# logging.basicConfig()

## 로그 포맷 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s     [%(levelname)s]     %(message)s'
)



## 2. 로거 객체 생성
logger = logging.getLogger(__name__)

userName = '홍길동'


## 3. 로그 출력
logger.debug('디버깅용 메시지')
logger.info(f'정보 메시지 :{userName}')
logger.info('정보 메시지: %s, %s ', userName, '박보검')
logger.warning('경고 메시지')
logger.error('에러 메시지')
logger.critical('치명적인 에러 메시지')

print('치명적인 에러 메시지')