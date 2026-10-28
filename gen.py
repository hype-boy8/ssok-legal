#!/usr/bin/env python3
"""쏙 개인정보 처리방침 · 이용약관 · 고객 지원 정적 페이지 생성기.

    python3 gen.py      # 이 폴더에 index.html · privacy.html · terms.html · support.html 을 만든다

문장은 이 파일 안에만 있다. 고칠 때는 여기를 고치고 다시 돌린다.
앱(data/Links.kt · iOS)과 Play Console · App Store Connect 가 이 주소를 가리킨다 — 주소(파일 이름)를 바꾸지 말 것.
    https://hype-boy8.github.io/ssok-legal/privacy.html   개인정보 처리방침
    https://hype-boy8.github.io/ssok-legal/terms.html     이용약관
    https://hype-boy8.github.io/ssok-legal/support.html   고객 지원(App Store Support URL)

문단 표기 규칙
    "문장"            → 문단
    ["항목", ...]     → 글머리표 목록
    "### 소제목"      → 작은 제목(안드로이드 / 아이폰처럼 플랫폼을 나눌 때)
    문장 속 https://… 주소와 메일 주소는 저절로 링크가 된다.
"""

import html
import pathlib
import re

OUT = pathlib.Path(__file__).resolve().parent
EFFECTIVE_KO = "2026년 10월 27일"
EFFECTIVE_EN = "October 27, 2026"
CONTACT = "planarfigure@gmail.com"
APP_KO = "쏙"
APP_EN = "ssok"
STORE_NAME_KO = "쏙 - 스크린샷 정리 · 캡처 보관함"
STORE_NAME_EN = "ssok - Screenshot Organizer"
APPLE_EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
APPLE_REFUND = "https://reportaproblem.apple.com"
PLAY_REFUND_KO = "https://support.google.com/googleplay/answer/2479637?hl=ko"
PLAY_REFUND_EN = "https://support.google.com/googleplay/answer/2479637?hl=en"

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0; background: #F8F6F2; color: #2B2433;
  font-family: -apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo',
               'Malgun Gothic', 'Noto Sans KR', sans-serif;
  line-height: 1.7; word-break: keep-all; overflow-wrap: anywhere;
}
.wrap { max-width: 720px; margin: 0 auto; padding: 40px 20px 80px; }
h1 { font-size: 26px; font-weight: 800; letter-spacing: -0.5px; margin: 0 0 6px; color: #5F3FBF; }
.meta { color: #6E6E76; font-size: 14px; margin: 0 0 32px; }
h2 { font-size: 17px; font-weight: 700; margin: 32px 0 8px; }
h3 { font-size: 15px; font-weight: 700; margin: 16px 0 4px; color: #2B2433; }
p, li { color: #51446B; font-size: 15px; }
p { margin: 0 0 8px; }
ul { margin: 0 0 8px; padding-left: 20px; }
a { color: #6A40CF; }
nav { margin: 0 0 32px; display: flex; gap: 8px; flex-wrap: wrap; }
nav a { padding: 8px 16px; border-radius: 999px; background: #fff; color: #2B2433;
        text-decoration: none; font-size: 14px; box-shadow: 0 1px 3px rgba(43,36,51,.08); }
nav a[aria-current] { background: #6A40CF; color: #fff; }
.lang { margin-top: 64px; padding-top: 24px; border-top: 1px solid #E6E6E6; }
footer { margin-top: 56px; color: #6E6E76; font-size: 13px; }
"""

# ── 개인정보 처리방침 ────────────────────────────────────────────────

PRIVACY_KO = [
    ("1. 요약",
     ["쏙(이하 \"앱\")은 나중에 쓸 스크린샷과 사진 기록을 휴대폰 안에서 정리하는 앱입니다. "
      "안드로이드(Google Play)와 아이폰(App Store)에서 제공하며, 이 방침은 두 앱 모두에 적용됩니다.",
      ["개발자는 이용자의 개인정보를 수집하지 않습니다. 개발자가 운영하는 서버가 없습니다.",
       "회원가입·로그인·광고·분석 도구·추적 기능이 없습니다.",
       "앱이 다루는 사진과 기록은 이용자의 기기 안에 저장되며, 개발자는 그 내용을 볼 수 없습니다."],
      "권한, 인터넷 연결, 백업처럼 플랫폼마다 다른 부분은 아래에 안드로이드와 아이폰으로 나눠 적었습니다."]),
    ("2. 개발자가 수집하는 정보",
     ["없습니다. 앱은 개발자에게 어떤 정보도 보내지 않습니다. "
      "이용자가 직접 개발자에게 메일을 보내는 경우에만 그 메일을 받게 됩니다(6항 참고)."]),
    ("3. 앱이 기기 안에 저장하는 정보",
     ["다음 정보는 이용자의 기기 안, 앱 전용 저장 공간에만 저장됩니다.",
      ["분류 기록: 어떤 사진을 어느 폴더에 넣었는지, 이용자가 정한 날짜·장소 이름, 끝냄 여부",
       "사진에서 읽은 글자: 검색과 날짜·장소 이름 후보를 위해 기기 안에서 읽은 글자 일부",
       "앱에서 찍은 사진: 앱 안 카메라로 찍은 기록 사진(갤러리나 사진 앱에는 저장되지 않습니다)",
       "설정값: 폴더 이름과 순서, 알림 시점, 화면 언어 등"],
      "### 안드로이드",
      "스크린샷 원본은 갤러리에 그대로 있습니다. 앱은 원본을 복사하거나 옮기지 않고 위치(주소)만 기억합니다.",
      "### 아이폰",
      ["사진 앱에 있는 사진은 복사하지 않고 사진 보관함의 참조(식별자)만 기억합니다.",
       "공유 메뉴나 단축어로 받은 사진 중 사진 앱에서 찾을 수 없는 사진, 그리고 앱 카메라로 찍은 사진은 앱 전용 공간에 사본으로 저장합니다.",
       "앱, 공유 메뉴의 쏙, 위젯이 같은 기록을 보도록 기기 안의 공유 저장 공간(App Group)을 씁니다. 이 공간도 기기 밖으로 나가지 않습니다."]]),
    ("4. 기기 안에서만 처리하는 기능",
     [["사진 속 글자·바코드 인식: 기기 안의 인식 기능으로 처리합니다(안드로이드는 기기 안 인식 모델, 아이폰은 Apple Vision).",
       "날짜·장소 이름 후보: 읽은 글자에서 후보를 고를 뿐이며, 이용자가 확인한 값만 알림과 기록에 씁니다.",
       "읽어주기(요리 모드): 기기에 설치된 음성 합성 기능을 사용합니다.",
       "음성 명령(요리 모드): 기기 안 음성 인식만 사용합니다. 기기가 이를 지원하지 않으면 음성 명령을 켜지 않습니다.",
       "알림: 기기 안에서 예약하는 알림입니다. 알림을 보내는 서버는 없습니다."]]),
    ("5. 요청하는 권한과 쓰는 곳",
     ["권한은 휴대폰 설정에서 언제든 끌 수 있습니다. 끈 권한과 관련된 기능만 멈추고 나머지는 계속 쓸 수 있습니다.",
      "### 안드로이드",
      ["사진: 새 스크린샷을 감지하고 담아 둔 사진을 보여 주기 위해",
       "알림: 캡처 직후 폴더 고르기, 날짜 알림, 감지 상태 표시를 위해",
       "다른 앱 위에 표시(선택): 캡처 직후 화면 구석에 폴더 버튼을 띄우기 위해",
       "카메라: 앱 안에서 기록 사진을 찍기 위해",
       "마이크: 요리 모드에서 \"다음\", \"다시\" 같은 짧은 음성 명령을 알아듣기 위해",
       "미디어 관리: 이용자가 \"갤러리에서 삭제\"를 고른 사진을 휴대폰 휴지통으로 옮기기 위해",
       "그 밖에 진동, 재부팅 후 감지 다시 켜기, 백그라운드 감지 유지, 네트워크 연결 상태 확인(인터넷 사용 권한이 아닙니다), Google Play 결제 연결"],
      "### 아이폰",
      ["사진: 담아 둔 사진을 보여 주고, 이용자가 고른 사진을 담기 위해. "
       "\"모든 사진\" 접근을 허용하고 \"앱을 열 때 새 스크린샷 모아오기\"를 켜면, 앱을 열 때 그 기능을 켠 뒤에 찍은 스크린샷을 찾습니다. "
       "\"선택한 사진\"만 허용하면 이용자가 고른 사진만 다룹니다.",
       "사진 추가: 이용자가 내보내기를 고른 기록 사진을 사진 앱에 저장하기 위해",
       "카메라: 앱 안에서 기록 사진을 찍기 위해",
       "마이크·음성 인식: 이용자가 요리 모드에서 음성 명령을 켰을 때만 짧은 명령을 알아듣기 위해",
       "알림: 날짜 알림과 요리 타이머를 위해"],
      "아이폰에서는 운영체제 특성상 스크린샷 직후 다른 앱 위에 버튼을 띄우지 않습니다. 사진은 공유 메뉴, 단축어, 앱 안 사진 고르기로 담습니다."]),
    ("6. 이용자가 직접 밖으로 보내는 경우",
     ["다음은 이용자가 직접 고를 때만 일어나며, 받는 쪽 서비스의 정책이 적용됩니다.",
      ["공유: 이용자가 고른 앱으로 사진이나 글이 전달됩니다.",
       "지도에서 열기: 장소 이름이 지도 앱(안드로이드는 이용자가 쓰는 지도 앱, 아이폰은 Apple 지도)으로 전달됩니다.",
       "백업 파일: 이용자가 고른 저장 위치에 파일이 만들어집니다. 그 위치가 클라우드라면 해당 서비스에 저장됩니다.",
       "개선 제안 메일: 메일 앱으로 보내면 개발자는 보낸 사람의 메일 주소와 내용, 함께 적힌 기기 정보(모델·운영체제 버전·앱 버전)를 받고 답장에만 씁니다. "
       "답장에 필요한 기간이 지나거나 삭제를 요청하면 지웁니다."]]),
    ("7. 인터넷 연결",
     ["### 안드로이드",
      "앱에는 인터넷 접근 권한이 없습니다. 쏙 프로 결제와 이용권 확인은 휴대폰에 설치된 Google Play 스토어 앱을 통해 이루어집니다.",
      "### 아이폰",
      "앱은 개발자의 서버와 통신하지 않습니다. 다만 다음 경우에는 Apple이 제공하는 기능이 Apple 서버에 연결될 수 있으며, Apple의 개인정보 처리방침이 적용됩니다.",
      ["구매·구독과 이용권 확인(StoreKit)",
       "iCloud 사진에만 있는 원본을 이용자가 열 때 원본 내려받기",
       "이용자가 \"지도에서 찾아보기\"를 누를 때 Apple 지도"]]),
    ("8. 구매",
     ["\"쏙 프로\"는 안드로이드에서는 Google Play, 아이폰에서는 App Store 결제로 구매합니다. "
      "결제 수단 등 결제 정보는 Google 또는 Apple이 처리하며 개발자에게 전달되지 않습니다. "
      "앱은 이용권이 있는지만 각 스토어를 통해 확인합니다. 개발자는 구매자의 이름이나 메일 주소를 받지 않습니다."]),
    ("9. 기기 백업",
     ["### 안드로이드",
      "앱 데이터는 안드로이드 기본 백업과 기기 간 이전에서 제외됩니다. 휴대폰을 바꿀 때는 앱에서 만든 백업 파일로 옮깁니다.",
      "### 아이폰",
      "앱 데이터는 이용자의 iCloud 백업이나 컴퓨터 백업에 포함될 수 있습니다. 이 백업은 이용자의 Apple 계정과 백업 설정에 따라 Apple 또는 이용자의 컴퓨터에 저장되며, 개발자는 접근할 수 없습니다."]),
    ("10. 보관과 삭제",
     [["앱을 삭제하면 앱 전용 공간의 기록, 앱에서 찍은 사진, 앱이 보관하던 사본이 모두 함께 지워집니다. "
       "아이폰에서는 이미 만들어진 iCloud·컴퓨터 백업에 그 백업의 보관 기간 동안 남을 수 있습니다.",
       "앱 안에서 \"쏙에서만 빼기\"를 고르면 쏙의 기록만 지우고 원본 사진은 그대로 둡니다.",
       "원본까지 지우기를 고르면, 안드로이드는 휴대폰 휴지통으로, 아이폰은 시스템 확인을 거쳐 사진 앱의 \"최근 삭제된 항목\"으로 옮겨집니다. 보통 30일 뒤 완전히 지워집니다.",
       "갤러리·사진 앱의 원본은 앱을 삭제해도 남습니다.",
       "개발자는 이용자 데이터를 따로 보관하지 않으므로 개발자에게 삭제를 요청할 데이터가 없습니다. 개발자에게 보낸 메일은 요청하면 지웁니다."]]),
    ("11. 아동의 개인정보",
     ["앱은 만 14세 미만 아동을 대상으로 하지 않으며, 아동을 포함한 누구의 개인정보도 수집하지 않습니다."]),
    ("12. 문의",
     [f"개인정보 처리에 관한 문의는 플래너피규어(Planar Figure) {CONTACT} 로 보내 주세요."]),
    ("13. 방침 변경",
     ["내용이 바뀌면 이 페이지의 시행일을 갱신하고, 중요한 변경은 앱 업데이트 안내에 함께 적습니다."]),
]

PRIVACY_EN = [
    ("1. Summary",
     ["ssok (the \"App\") organizes screenshots and photo notes you will use later, on your phone. "
      "It is available for Android (Google Play) and iPhone (App Store), and this policy covers both.",
      ["The developer does not collect any personal information. The developer runs no servers.",
       "There is no sign-up, no login, no advertising, no analytics and no tracking.",
       "Your photos and records stay on your device, and the developer cannot see them."],
      "Where the platforms differ, such as permissions, internet access and backups, Android and iPhone are described separately below."]),
    ("2. Information collected by the developer",
     ["None. The App sends nothing to the developer. The developer only receives an email if you choose to send one (see section 6)."]),
    ("3. What the App stores on your device",
     ["The following is stored only in the App's private storage on your device.",
      ["Filing records: which photo went to which folder, dates and place names you set, and whether an item is finished",
       "Text read from photos: part of the text recognized on the device, used for search and for date and place-name suggestions",
       "Photos taken in the App: photo notes taken with the in-app camera (not saved to your gallery or Photos library)",
       "Settings: folder names and order, reminder timing, display language and so on"],
      "### Android",
      "Original screenshots stay in your gallery. The App never copies or moves them; it only remembers where they are.",
      "### iPhone",
      ["Photos already in your Photos library are not copied. The App only keeps a reference (identifier) to them.",
       "Photos received through the share sheet or Shortcuts that cannot be found in your Photos library, and photos taken with the in-app camera, are saved as copies in the App's private storage.",
       "The App, the ssok share extension and the widgets use a shared storage area on the device (App Group) so they see the same records. It also stays on your device."]]),
    ("4. Processed on the device only",
     [["Text and barcode recognition runs on the device (an on-device model on Android, Apple Vision on iPhone).",
       "Date and place-name suggestions are only suggestions taken from the recognized text. Only values you confirm are used for reminders and records.",
       "Read-aloud (cooking mode) uses the speech voices installed on your device.",
       "Voice commands (cooking mode) use on-device speech recognition only. If your device does not support it, voice commands stay off.",
       "Notifications are scheduled locally on the device. There is no push server."]]),
    ("5. Permissions and why",
     ["You can turn permissions off at any time in your phone settings. Only the related feature stops.",
      "### Android",
      ["Photos: to detect new screenshots and show the photos you saved",
       "Notifications: to pick a folder right after a capture, for date reminders and to show detection status",
       "Display over other apps (optional): to show folder buttons in a corner right after a capture",
       "Camera: to take photo notes inside the App",
       "Microphone: to understand short voice commands such as \"next\" or \"again\" in cooking mode",
       "Media management: to move photos you chose to delete from the gallery into your phone's trash",
       "Also: vibration, restarting detection after reboot, keeping detection running, checking network status (this is not internet access), Google Play billing"],
      "### iPhone",
      ["Photos: to show the photos you saved and to add the photos you pick. "
       "If you allow access to all photos and turn on \"Collect new screenshots when you open ssok\", the App looks for screenshots taken after you turned it on, when you open the App. "
       "With limited access, the App only handles the photos you select.",
       "Add to Photos: to save record photos you choose to export to your Photos library",
       "Camera: to take photo notes inside the App",
       "Microphone and speech recognition: only when you turn on voice commands in cooking mode",
       "Notifications: for date reminders and cooking timers"],
      "On iPhone, the system does not let apps show buttons over other apps right after a screenshot. You add photos through the share sheet, Shortcuts or the in-app photo picker."]),
    ("6. When you send something out yourself",
     ["These happen only when you choose them, and the receiving service's policy applies.",
      ["Share: photos or text go to the app you pick.",
       "Open in Maps: the place name goes to a map app (your map app on Android, Apple Maps on iPhone).",
       "Backup file: a file is created at the location you pick. If that location is a cloud service, the file is stored there.",
       "Feedback email: if you send it, the developer receives your email address, the message and the device details included (model, OS version, app version), used only to reply. "
       "It is deleted once no longer needed for the reply, or on request."]]),
    ("7. Internet access",
     ["### Android",
      "The App has no internet permission. ssok Pro purchases and access checks go through the Google Play Store app on your phone.",
      "### iPhone",
      "The App does not communicate with any developer server. Apple's own frameworks may connect to Apple in the following cases, and Apple's privacy policy applies:",
      ["Purchases, subscriptions and access checks (StoreKit)",
       "Downloading an original that is stored only in iCloud Photos, when you open it",
       "Apple Maps, when you tap \"Find on Maps\""]]),
    ("8. Purchases",
     ["\"ssok Pro\" is purchased through Google Play on Android and through the App Store on iPhone. "
      "Payment details are handled by Google or Apple and are not shared with the developer. "
      "The App only checks with the store whether you have access. The developer does not receive the buyer's name or email address."]),
    ("9. Device backups",
     ["### Android",
      "App data is excluded from Android's built-in backup and device-to-device transfer. To move to a new phone, use the backup file made in the App.",
      "### iPhone",
      "App data may be included in your own iCloud or computer backup. That backup is stored by Apple or on your computer according to your Apple Account and backup settings, and the developer cannot access it."]),
    ("10. Retention and deletion",
     [["Deleting the App deletes its records, photos taken in the App and copies it kept. "
       "On iPhone, they may remain in iCloud or computer backups made earlier, for as long as those backups are kept.",
       "\"Remove from ssok only\" deletes the record in ssok and leaves the original photo as it is.",
       "If you choose to delete the original too, it moves to your phone's trash on Android, or, after the system's confirmation, to \"Recently Deleted\" in Photos on iPhone. It is usually removed for good after 30 days.",
       "Originals in your gallery or Photos library remain when you delete the App.",
       "The developer keeps no copy of your data, so there is nothing to request deletion of from the developer. Emails you sent to the developer are deleted on request."]]),
    ("11. Children",
     ["The App is not directed to children under 14 and does not collect personal information from anyone, including children."]),
    ("12. Contact",
     [f"Questions about privacy: Planar Figure, {CONTACT}"]),
    ("13. Changes",
     ["If this policy changes, the effective date on this page is updated. Important changes are also noted in app update notes."]),
]

# ── 이용약관 ─────────────────────────────────────────────────────────

TERMS_KO = [
    ("1. 목적",
     ["이 약관은 플래너피규어(Planar Figure, 이하 \"개발자\")가 제공하는 쏙(이하 \"앱\")의 안드로이드판과 아이폰판을 이용하는 데 필요한 사항을 정합니다. "
      "앱을 설치해 사용하면 이 약관에 동의한 것으로 봅니다."]),
    ("2. 서비스 내용",
     ["앱은 이용자의 기기 안에서 스크린샷을 폴더로 정리하고, 날짜 알림·검색·요리 모드·사진 기록·위젯·백업 파일 같은 기능을 제공하는 도구입니다. "
      "별도 서버나 계정 없이 기기 안에서 동작합니다."]),
    ("3. 쏙 프로와 계속 쓸 수 있는 기능",
     [["새 캡처를 담고 새 기록을 시작하려면 \"쏙 프로\" 이용권이 필요합니다.",
       "이용권이 없어도 이미 담은 것을 열고, 꺼내 쓰고, 끝내고, 삭제할 수 있습니다. 날짜 알림, 요리 모드, 폴더 만들기, 이미 시작한 기록에 사진 추가하기도 계속 쓸 수 있습니다.",
       "쏙 프로는 월 구독과 평생 구매 두 가지이며, 제공하는 기능은 같습니다. 한국 기준 월 구독은 월 2,000원, 평생 구매는 15,000원입니다. "
       "다른 국가의 통화·세금·최종 가격은 각 스토어의 구매 화면에 표시됩니다.",
       "앱 자체에서 따로 운영하는 무료 체험 기간은 없습니다."]]),
    ("4. 월 구독: 첫 달 무료와 자동 갱신",
     [["월 구독을 처음 시작하는 이용자는 첫 달을 무료로 쓸 수 있습니다. 첫 달 무료는 스토어 계정당 한 번이며, 받을 수 있는지는 각 스토어가 정합니다"
       "(Google Play의 무료 체험, App Store의 첫 구독 혜택).",
       "무료 기간이 끝나면 해지하지 않는 한 유료 구독으로 자동 전환되고, 이후 매월 자동 갱신되며 요금이 청구됩니다.",
       "Google Play: 무료 체험이 끝나기 전에 해지하면 요금이 청구되지 않습니다. 해지는 Google Play 앱 → 프로필 → 결제 및 정기 결제 → 정기 결제에서 할 수 있습니다.",
       "App Store: 무료 기간을 포함해 현재 기간이 끝나기 최소 24시간 전에 해지하지 않으면 자동으로 갱신되며, 기간이 끝나기 전 24시간 안에 다음 기간 요금이 Apple 계정으로 청구됩니다. "
       "해지는 설정 → Apple 계정 → 구독에서 할 수 있습니다.",
       "해지해도 이미 결제한 기간(또는 남은 무료 기간)이 끝날 때까지 이용할 수 있고, 그 뒤로는 갱신되지 않습니다. 앱 삭제만으로는 구독이 해지되지 않습니다.",
       "안드로이드판은 월 구독 이용권을 확인하기 위해 24시간에 한 번 Google Play에 연결합니다. 확인하지 못해 새로 담기가 잠시 멈춰도 기존 자료는 계속 열 수 있습니다.",
       "구독 가격이 바뀌면 각 스토어의 절차에 따라 미리 알립니다."]]),
    ("5. 평생 구매",
     [["평생 구매는 한 번만 결제하며 자동 갱신이나 정기 청구가 없습니다.",
       "월 구독을 쓰다가 평생 구매로 바꾸려면 월 구독을 따로 해지해 주세요. 월 구독은 평생 구매로 자동 전환되거나 남은 기간이 환불되지 않습니다."]]),
    ("6. 구매 복원과 플랫폼",
     [["구매는 구매에 쓴 Google 계정 또는 Apple 계정에 기록됩니다. 같은 계정으로 다시 설치하면 안드로이드는 \"구매 내역 다시 불러오기\", 아이폰은 \"구매 복원\"으로 되살릴 수 있습니다.",
       "안드로이드(Google Play)에서 구매한 이용권은 아이폰에서 쓸 수 없고, 아이폰(App Store)에서 구매한 이용권도 안드로이드에서 쓸 수 없습니다."]]),
    ("7. 결제와 환불",
     ["결제는 Google 또는 Apple이 처리하며, 환불은 각 스토어의 정책과 절차를 따릅니다. 개발자는 결제를 직접 처리하지 않아 환불을 대신 승인할 수 없습니다.",
      [f"Google Play: Google Play 환불 정책에 따라 요청할 수 있습니다. {PLAY_REFUND_KO}",
       f"App Store: Apple의 문제 신고 페이지에서 요청할 수 있습니다. {APPLE_REFUND}"],
      "관련 법령이 보장하는 이용자의 청약 철회 등 권리는 이 약관으로 제한되지 않습니다."]),
    ("8. 아이폰판과 Apple 표준 사용권 계약",
     [f"App Store에서 받은 앱에는 이 약관과 함께 Apple의 표준 최종 사용자 사용권 계약(EULA)이 적용됩니다. {APPLE_EULA}"]),
    ("9. 인식 결과와 알림의 한계",
     ["사진에서 읽은 날짜·장소 이름·재료와 조리 순서는 자동 인식이라 틀릴 수 있으며, 개발자는 그 정확성을 보장하지 않습니다. "
      "앱이 보여 주는 날짜는 후보일 뿐이고 이용자가 확인한 값만 알림에 씁니다. 쿠폰 만료일이나 예약 날짜 같은 중요한 정보는 원본에서 직접 확인해 주세요. "
      "알림은 기기의 절전·알림 설정에 따라 늦거나 오지 않을 수 있습니다."]),
    ("10. 사진 기록의 성격",
     ["앱에서 찍은 사진에 표시되는 시각과 기록은 이용자의 기억을 돕기 위한 것이며, 법적 증거로서의 효력을 보장하지 않습니다."]),
    ("11. 이용자의 책임",
     [["원본까지 지우기를 고르면 안드로이드는 휴대폰 휴지통으로, 아이폰은 사진 앱의 \"최근 삭제된 항목\"으로 옮겨집니다. 그곳에서도 지워지면 되살릴 수 없습니다.",
       "앱에서 찍은 사진은 앱 전용 공간에 있어 앱을 삭제하면 함께 지워집니다. 남겨야 할 것은 미리 공유하거나 백업 파일로 내보내 주세요.",
       "휴대폰을 바꿀 때는 앱 설정에서 백업 파일을 만들어 새 휴대폰에서 가져와 주세요."]]),
    ("12. 보증의 부인과 책임의 제한",
     ["앱은 제공되는 상태 그대로 제공됩니다. 법령이 허용하는 범위에서, 앱 이용 중 생긴 데이터 손실이나 인식·알림 오류로 인한 손해에 대해 개발자는 책임을 지지 않습니다. "
      "다만 개발자의 고의 또는 중대한 과실로 생긴 손해는 예외입니다."]),
    ("13. 서비스 변경",
     ["기능은 앱 업데이트로 바뀔 수 있습니다. 이미 구매한 평생 구매의 혜택(새로 담기)은 줄이지 않습니다."]),
    ("14. 문의",
     [f"약관에 관한 문의는 {CONTACT} 로 보내 주세요."]),
]

TERMS_EN = [
    ("1. Purpose",
     ["These terms govern your use of ssok (the \"App\") for Android and iPhone, provided by Planar Figure (the \"developer\"). "
      "By installing and using the App you agree to them."]),
    ("2. The service",
     ["The App organizes screenshots into folders on your device and offers date reminders, search, cooking mode, photo notes, widgets and backup files. "
      "It works on your device, with no server and no account."]),
    ("3. ssok Pro and what stays available",
     [["Adding new captures and starting new records requires \"ssok Pro\" access.",
       "Without it, you can still open, use, finish and delete what you already saved. Date reminders, cooking mode, making folders and adding photos to a record you already started also keep working.",
       "ssok Pro comes as a monthly subscription or a lifetime purchase with the same features. In South Korea, the monthly subscription is KRW 2,000 per month and the lifetime purchase is KRW 15,000. "
       "Local currency, taxes and the final price are shown on the store's purchase screen.",
       "The App does not run a separate trial period of its own."]]),
    ("4. Monthly subscription: free first month and auto-renewal",
     [["New subscribers can use the first month free. The free month is available once per store account, and eligibility is decided by the store "
       "(a Google Play free trial or an App Store introductory offer).",
       "When the free month ends, the subscription converts to a paid subscription and renews automatically every month unless you cancel.",
       "Google Play: cancel before the free trial ends and you will not be charged. Cancel in the Google Play app → profile → Payments & subscriptions → Subscriptions.",
       "App Store: the subscription renews automatically unless cancelled at least 24 hours before the end of the current period, including the free month. "
       "Your Apple Account is charged for the next period within 24 hours before the current period ends. Cancel in Settings → Apple Account → Subscriptions.",
       "After cancelling, access continues until the end of the paid period (or the remaining free month), with no further renewal. Deleting the App does not cancel a subscription.",
       "On Android, the App checks monthly access with Google Play once every 24 hours. If it cannot check, adding new items may pause, while saved items remain available.",
       "If the subscription price changes, you will be notified in advance according to each store's process."]]),
    ("5. Lifetime purchase",
     [["The lifetime purchase is a one-time payment with no automatic renewal or recurring charges.",
       "To switch from monthly to lifetime, cancel the monthly subscription separately. It is not converted into the lifetime purchase, and the remaining period is not refunded automatically."]]),
    ("6. Restoring purchases and platforms",
     [["Purchases are tied to the Google account or Apple Account used to buy them. Reinstall with the same account and use \"Restore purchase\" (Android) or \"Restore purchases\" (iPhone).",
       "Access bought on Android (Google Play) cannot be used on iPhone, and access bought on iPhone (App Store) cannot be used on Android."]]),
    ("7. Payments and refunds",
     ["Payments are processed by Google or Apple, and refunds follow each store's policies and procedures. The developer does not process payments and cannot grant refunds on the store's behalf.",
      [f"Google Play: request a refund under Google Play's refund policy. {PLAY_REFUND_EN}",
       f"App Store: request a refund on Apple's Report a Problem page. {APPLE_REFUND}"],
      "Nothing in these terms limits any right you have under applicable consumer law, such as a right of withdrawal."]),
    ("8. iPhone version and Apple's standard EULA",
     [f"For the App obtained from the App Store, Apple's Licensed Application End User License Agreement (standard EULA) applies in addition to these terms. {APPLE_EULA}"]),
    ("9. Limits of recognition and reminders",
     ["Dates, place names, ingredients and recipe steps read from photos are recognized automatically and can be wrong. The developer does not warrant their accuracy. "
      "Dates shown by the App are suggestions; only values you confirm are used for reminders. Please check important details such as coupon expiry or booking dates in the original. "
      "Reminders may be late or missing depending on your device's battery and notification settings."]),
    ("10. Nature of photo notes",
     ["Times and notes shown on photos taken in the App are there to help you remember. They are not guaranteed to have any legal effect as evidence."]),
    ("11. Your responsibilities",
     [["If you choose to delete an original, it moves to your phone's trash on Android, or to \"Recently Deleted\" in Photos on iPhone. Once removed from there, it cannot be restored.",
       "Photos taken in the App live in its private storage and are deleted when the App is deleted. Share or export a backup file first if you need to keep them.",
       "When changing phones, create a backup file in the App's settings and import it on the new phone."]]),
    ("12. Disclaimer and limitation of liability",
     ["The App is provided \"as is\". To the extent permitted by law, the developer is not liable for data loss or for damage caused by recognition or reminder errors, "
      "except where caused by the developer's intent or gross negligence."]),
    ("13. Changes",
     ["Features may change through app updates. The benefit of a lifetime purchase already made (adding new items) will not be reduced."]),
    ("14. Contact",
     [f"Questions about these terms: {CONTACT}"]),
]

# ── 고객 지원 ────────────────────────────────────────────────────────

SUPPORT_KO = [
    ("문의하기",
     [f"사용 중 궁금한 점, 오류, 개선 제안은 {CONTACT} 로 보내 주세요. 쓰고 있는 휴대폰 기종과 운영체제 버전, 앱 버전을 함께 적어 주시면 더 빨리 도와드릴 수 있어요. "
      "앱 설정의 \"개선 제안 보내기\"(안드로이드)나 \"문의·의견 보내기\"(아이폰)로도 메일을 쓸 수 있어요."]),
    ("안드로이드에서 스크린샷은 어떻게 담나요?",
     [["설정에서 스크린샷 감지를 켜 두면, 캡처하는 순간 화면 구석의 폴더 버튼이나 알림에서 폴더를 고를 수 있어요(폴더 버튼은 \"다른 앱 위에 표시\"를 허용했을 때 떠요).",
       "고르지 않고 넘긴 캡처는 미분류에 모여 있어 나중에 정리할 수 있어요.",
       "예전에 찍어 둔 스크린샷은 갤러리에서 공유 → \"쏙에 담기\"로 넣을 수 있어요."]]),
    ("아이폰에서는 어떻게 담나요?",
     ["아이폰은 운영체제 특성상 스크린샷 직후 다른 앱 위에 버튼을 띄울 수 없어요. 대신 다음 방법으로 담아요.",
      ["공유 메뉴: 사진 앱이나 스크린샷 미리보기에서 공유 버튼 → ssok",
       "단축어: 단축어 앱의 \"쏙에 담기\" 동작으로 사진을 바로 담을 수 있어요",
       "앱 안에서: 사진 고르기로 필요한 사진만 담기",
       "앱을 열 때 모아오기: \"모든 사진\" 접근을 허용하고 \"앱을 열 때 새 스크린샷 모아오기\"를 켜면, 켠 뒤에 찍은 스크린샷을 앱을 열 때 미분류로 모아 와요"]]),
    ("쏙 프로 없이 쓸 수 있는 기능은요?",
     ["새 캡처를 담고 새 기록을 시작할 때만 쏙 프로가 필요해요. 이미 담은 것 열기·꺼내 쓰기·끝내기·삭제, 날짜 알림, 요리 모드, 폴더 만들기, "
      "이미 시작한 기록에 사진 추가는 이용권이 없어도 계속 돼요. 광고는 없어요."]),
    ("첫 달 무료는 어떻게 되나요?",
     ["월 구독(한국 기준 월 2,000원)을 처음 시작하면 첫 달이 무료예요. 스토어 계정당 한 번이고, 무료 달이 끝나면 해지하지 않는 한 매월 자동 갱신돼요. "
      "결제를 원하지 않으면 안드로이드는 무료 기간이 끝나기 전에, 아이폰은 끝나기 최소 24시간 전에 해지해 주세요. "
      "한 번만 결제하고 싶다면 평생 구매(한국 기준 15,000원)를 고르면 돼요. 두 상품의 기능은 같아요."]),
    ("구독은 어떻게 해지하나요?",
     ["### 안드로이드",
      "Google Play 앱 → 오른쪽 위 프로필 → 결제 및 정기 결제 → 정기 결제 → 쏙 → 정기 결제 취소.",
      "### 아이폰",
      "설정 → Apple 계정(맨 위 이름) → 구독 → ssok → 구독 취소. 앱의 쏙 프로 화면에서 \"구독 관리\"를 눌러도 같은 화면이 열려요.",
      "앱을 삭제하는 것만으로는 구독이 해지되지 않아요. 해지해도 결제한 기간이 끝날 때까지는 계속 쓸 수 있어요."]),
    ("구매를 다시 불러오려면요?",
     ["구매에 쓴 같은 계정으로 로그인한 상태에서, 안드로이드는 쏙 프로 화면의 \"구매 내역 다시 불러오기\", 아이폰은 \"구매 복원\"을 눌러 주세요. "
      "안드로이드에서 구매한 이용권은 아이폰에서, 아이폰에서 구매한 이용권은 안드로이드에서 쓸 수 없어요."]),
    ("환불은 어디서 하나요?",
     ["결제는 Google과 Apple이 처리해서 환불도 각 스토어에서 요청해요.",
      [f"Google Play: {PLAY_REFUND_KO}",
       f"App Store: {APPLE_REFUND}"]]),
    ("새 휴대폰으로 옮기려면요?",
     ["앱 설정의 \"폰을 바꿀 때\"(안드로이드)나 \"백업·복원\"(아이폰)에서 \"백업 파일 만들기\"로 파일을 저장하고, 새 휴대폰에서 같은 곳의 가져오기로 불러와 주세요. "
      "기록, 폴더, 쏙에서 찍은 사진이 함께 옮겨져요. 갤러리·사진 앱의 스크린샷 원본은 백업 파일에 들어가지 않으니 따로 옮겨 주세요. "
      "새 휴대폰에 같은 사진이 있으면 다시 이어 붙여요. 구매는 백업 파일이 아니라 스토어 계정으로 복원해요."]),
    ("날짜를 왜 확인하라고 하나요?",
     ["쿠폰이나 예약 화면에는 유효기간 말고도 주문일, 발행일, 결제일 같은 날짜가 함께 있어요. 쏙은 캡처 속 글자를 기기 안에서 읽어 날짜 후보를 보여 줄 뿐, "
      "저절로 확정하지 않아요. 맞는 날짜를 확인해 주시면 그 날짜로 알림을 드려요. 틀린 후보는 직접 고칠 수 있어요."]),
    ("알림이 오지 않아요",
     [["휴대폰 설정에서 쏙의 알림이 켜져 있는지 확인해 주세요.",
       "안드로이드는 배터리 최적화가 앱을 멈추게 할 수 있어요. 앱 설정의 권한 목록에서 배터리 항목을 눌러 \"제한 없음\"으로 두면 감지와 알림이 안정적이에요.",
       "날짜 알림 시점은 앱 설정의 \"날짜 알림\"에서 고를 수 있어요."]]),
    ("내 사진은 어디에 저장되나요?",
     ["모두 휴대폰 안에 있어요. 개발자 서버가 없고, 로그인·광고·분석 도구도 없어요. 자세한 내용은 개인정보 처리방침을 확인해 주세요."]),
]

SUPPORT_EN = [
    ("Contact",
     [f"For questions, problems or suggestions, email {CONTACT}. Including your phone model, OS version and app version helps us help you faster. "
      "You can also write from \"Send feedback\" (Android) or \"Contact and feedback\" (iPhone) in the App's settings."]),
    ("How do I save screenshots on Android?",
     [["Turn on screenshot detection in Settings. When you take a screenshot, pick a folder from the folder buttons in the corner of the screen or from the notification (the buttons appear when \"Display over other apps\" is allowed).",
       "Screenshots you skip are kept in Unsorted so you can file them later.",
       "For older screenshots, share them from your gallery → \"Keep in ssok\"."]]),
    ("How do I save on iPhone?",
     ["iPhone does not let apps show buttons over other apps right after a screenshot. Instead, you can:",
      ["Share sheet: tap Share in Photos or on the screenshot preview → ssok",
       "Shortcuts: use the \"Save to ssok\" action in the Shortcuts app to save a photo directly",
       "In the App: choose only the photos you need with the photo picker",
       "Collect on open: allow access to all photos and turn on \"Collect new screenshots when you open ssok\". Screenshots taken after you turn it on are gathered into Unsorted when you open the App"]]),
    ("What can I use without ssok Pro?",
     ["ssok Pro is needed only to add new captures and start new records. Opening, using, finishing and deleting saved items, date reminders, cooking mode, making folders "
      "and adding photos to a record you already started keep working without it. There are no ads."]),
    ("How does the free first month work?",
     ["When you start the monthly subscription (KRW 2,000 per month in South Korea; local prices are shown in the store) for the first time, the first month is free. "
      "It is available once per store account. After the free month, the subscription renews every month unless you cancel. "
      "To avoid being charged, cancel before the free trial ends on Android, or at least 24 hours before it ends on iPhone. "
      "If you prefer to pay once, choose the lifetime purchase (KRW 15,000 in South Korea). Both offer the same features."]),
    ("How do I cancel my subscription?",
     ["### Android",
      "Google Play app → profile icon (top right) → Payments & subscriptions → Subscriptions → ssok → Cancel subscription.",
      "### iPhone",
      "Settings → Apple Account (your name at the top) → Subscriptions → ssok → Cancel Subscription. \"Manage subscription\" on the ssok Pro screen opens the same page.",
      "Deleting the App does not cancel a subscription. After cancelling, you keep access until the end of the paid period."]),
    ("How do I restore a purchase?",
     ["While signed in with the account you bought with, tap \"Restore purchase\" on the ssok Pro screen on Android, or \"Restore purchases\" on iPhone. "
      "Access bought on Android cannot be used on iPhone, and access bought on iPhone cannot be used on Android."]),
    ("Where do I ask for a refund?",
     ["Payments are handled by Google and Apple, so refunds are requested from each store.",
      [f"Google Play: {PLAY_REFUND_EN}",
       f"App Store: {APPLE_REFUND}"]]),
    ("How do I move to a new phone?",
     ["In the App's settings (\"Switching phones\" on Android, \"Backup and restore\" on iPhone), make a backup file and save it, then restore it from the same place on the new phone. "
      "Records, folders and photos taken in ssok come along. Original screenshots in your gallery or Photos library are not inside the backup file, so move them separately; "
      "if the same photos are on the new phone, ssok links them again. Purchases are restored through your store account, not the backup file."]),
    ("Why do I need to confirm dates?",
     ["Coupon and booking screens often show several dates, such as the order date, issue date or payment date, besides the expiry date. "
      "ssok reads the text on the device and only suggests dates; it never confirms them on its own. Once you confirm the right date, reminders use it. You can correct a wrong suggestion yourself."]),
    ("I am not getting reminders",
     [["Check that notifications for ssok are allowed in your phone settings.",
       "On Android, battery optimization may stop the App. Tap the battery item in the App's permission list and set it to \"Unrestricted\" for reliable detection and reminders.",
       "You can choose when date reminders arrive under \"Date reminders\" in the App's settings."]]),
    ("Where are my photos stored?",
     ["Everything stays on your phone. There is no developer server, no login, no ads and no analytics. See the Privacy Policy for details."]),
]


def esc(s):
    return html.escape(s, quote=False)


LINK = re.compile(r"(https://[^\s)]+[^\s).,]|[\w.+-]+@[\w-]+\.[\w.]+[^\s.,])")


def linkify(s):
    """이미 이스케이프한 문장에서 주소와 메일을 링크로."""
    def rep(m):
        t = m.group(0)
        href = t if t.startswith("https://") else f"mailto:{t}"
        return f'<a href="{href}">{t}</a>'
    return LINK.sub(rep, s)


def text(s):
    return linkify(esc(s))


def body(sections):
    out = []
    for title, parts in sections:
        out.append(f"<h2>{esc(title)}</h2>")
        for p in parts:
            if isinstance(p, list):
                out.append("<ul>" + "".join(f"<li>{text(i)}</li>" for i in p) + "</ul>")
            elif p.startswith("### "):
                out.append(f"<h3>{esc(p[4:])}</h3>")
            else:
                out.append(f"<p>{text(p)}</p>")
    return "\n".join(out)


def nav(current):
    items = [("index.html", "홈 · Home"), ("support.html", "고객 지원 · Support"),
             ("privacy.html", "개인정보 처리방침 · Privacy"), ("terms.html", "이용약관 · Terms")]
    return "<nav>" + "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{esc(t)}</a>' for h, t in items
    ) + "</nav>"


def page(file, title, inner):
    doc = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>{CSS}</style>
</head>
<body><div class="wrap">
{nav(file)}
{inner}
<footer>운영 · Operated by 플래너피규어(Planar Figure)<br>문의 · Contact <a href="mailto:{CONTACT}">{CONTACT}</a></footer>
</div></body>
</html>
"""
    (OUT / file).write_text(doc, encoding="utf-8")


def bilingual(file, ko_title, en_title, ko, en, dated=True):
    meta_ko = f"{APP_KO} · 시행일 {EFFECTIVE_KO}" if dated else f"{APP_KO} · 안드로이드 · 아이폰"
    meta_en = f"{APP_EN} · Effective {EFFECTIVE_EN}" if dated else f"{APP_EN} · Android · iPhone"
    page(file, f"{ko_title} · {APP_KO}", f"""
<h1>{esc(ko_title)}</h1>
<p class="meta">{meta_ko} · <a href="#en">English</a></p>
{body(ko)}
<div class="lang" id="en">
<h1>{esc(en_title)}</h1>
<p class="meta">{meta_en}</p>
{body(en)}
</div>""")


page("index.html", f"{APP_KO} · {APP_EN}", f"""
<h1>{esc(APP_KO)}</h1>
<p class="meta">Google Play · App Store: {esc(STORE_NAME_KO)} / {esc(STORE_NAME_EN)}</p>
<p>쿠폰·티켓, 가볼 곳, 레시피, 할 것처럼 나중에 쓸 스크린샷을 폴더에 쏙 모으고, 주차 위치와 영수증 같은 사진 기록을 남기는 앱이에요. 안드로이드와 아이폰에서 쓸 수 있어요. 캡처 속 글자는 휴대폰 안에서 읽고, 개발자 서버나 로그인·광고가 없어 사진이 개발자에게 전달되지 않아요.</p>
<p>An app for Android and iPhone that collects screenshots you will use later, such as coupons, tickets, places, recipes and to-dos, into folders, and keeps photo notes such as where you parked or your receipts. Text in captures is read on your phone, and with no developer server, no login and no ads, your photos are never sent to the developer.</p>
<ul>
<li><a href="support.html">고객 지원 · Support</a></li>
<li><a href="privacy.html">개인정보 처리방침 · Privacy Policy</a></li>
<li><a href="terms.html">이용약관 · Terms of Use</a></li>
</ul>""")

bilingual("support.html", "고객 지원", "Support", SUPPORT_KO, SUPPORT_EN, dated=False)
bilingual("privacy.html", "개인정보 처리방침", "Privacy Policy", PRIVACY_KO, PRIVACY_EN)
bilingual("terms.html", "이용약관", "Terms of Use", TERMS_KO, TERMS_EN)
print("ok")
