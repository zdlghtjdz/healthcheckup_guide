# healthcheckup_guide

이 프로젝트는 SKT와 함께하는 AI기반 인력양성 교육을 통해 진행되었습니다.
프로젝트 참여 인원은 이호성, 이준형, 강지윤, 김지헌입니다.

프로젝트 주제는 NUGU AI 스피커를 활용한 건강검진 가이드 앱 제작입니다.

건강검진 가이드 앱은 3개의 기능을 가지고 있습니다.

1. 건강검진에 대한 발화에 대한 처리(ex. 폐암 검진에 대해서 알려줘) - 구현중
2. 생년월일과 성별에 대한 해당되는 건강검진 여부(ex. 1995년 10월 23일 남자에 대한 건강검진 알려줘.)
3. 건강검진에 대한 주의사항(ex. 건강검진에서 주의할 사항은 뭐야?) - 미구현

각 기능에 대한 FLOW는 다음과 같은 형태입니다.

![그림1.png](https://github.com/zdlghtjdz/healthcheckup_guide/blob/main/그림1.png)
![그림2.png](https://github.com/zdlghtjdz/healthcheckup_guide/blob/main/그림2.png)

---

Nugu Play의 구조는 다음과 같습니다.

![그림3.png](https://github.com/zdlghtjdz/healthcheckup_guide/blob/main/%EA%B7%B8%EB%A6%BC3.PNG)

---

github를 통해 관리되는 소스코드는 Nugu Play에서 사용하기 위한 API 서버 및 DB 관련 코드입니다.
웹서버는 아마존 AWS에서 Flask를 통해 동작합니다. 
Nugu Play로 부터 정의된 요청(POST방식)이 오면, 그에 대한 응답을 json형태로 반환하게 됩니다.

해당 프로젝트에 대한 문의사항이나 궁금한 점이 있으시면 zdlghtjdz@naver.com으로 메일 보내주시면 감사하겠습니다.
