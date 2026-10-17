#!/usr/bin/env python3
"""쏙 개인정보 처리방침 · 이용약관 정적 페이지 생성기.

    python3 gen.py      # 이 폴더에 index.html · privacy.html · terms.html 을 만든다

문장은 이 파일 안에만 있다. 고칠 때는 여기를 고치고 다시 돌린다.
앱(data/Links.kt)과 Play Console 스토어 등록정보가 이 주소를 가리킨다 — 주소(파일 이름)를 바꾸지 말 것.
"""

import html
import pathlib

OUT = pathlib.Path(__file__).resolve().parent
EFFECTIVE_KO = "2026년 10월 17일"
EFFECTIVE_EN = "October 17, 2026"
CONTACT = "zxcvzxcv4423@gmail.com"
APP_KO = "쏙"
APP_EN = "ssok"
PLAY_NAME_KO = "쏙 - 스크린샷 정리와 사진 기록"
PLAY_NAME_EN = "ssok - Screenshots & Notes"

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
      "앱에는 인터넷 접근 권한이 없습니다. 앱이 다루는 사진과 기록은 이용자의 휴대폰 밖으로 "
      "전송되지 않으며, 개발자는 그 내용을 볼 수 없습니다. 회원가입·로그인·광고·분석 도구가 없습니다."]),
    ("2. 앱이 다루는 정보와 저장 위치",
     ["모든 정보는 이용자의 휴대폰 안, 앱 전용 저장 공간에만 저장됩니다.",
      ["분류 기록: 어떤 스크린샷을 어느 폴더에 넣었는지, 날짜·장소 이름 같은 이용자가 정한 값, 끝냄 여부",
       "사진에서 읽은 글자: 검색과 날짜 인식을 위해 기기 안에서 읽은 글자 일부",
       "앱에서 찍은 사진: 앱 안 카메라로 찍은 기록 사진(갤러리에는 저장되지 않습니다)",
       "설정값: 폴더 이름과 순서, 알림 시점, 화면 언어 등"],
      "스크린샷 원본은 갤러리에 그대로 있으며, 앱은 원본을 복사하거나 옮기지 않고 위치(주소)만 기억합니다."]),
    ("3. 기기 안에서만 처리하는 기능",
     [["사진 속 글자·바코드 인식: 기기 안의 인식 모델로 처리합니다.",
       "읽어주기: 휴대폰의 음성 합성 기능을 사용합니다.",
       "음성 명령(요리 모드): 기기 안 음성 인식만 사용하며, 기기가 이를 지원하지 않으면 음성 명령을 켜지 않습니다."]]),
    ("4. 요청하는 권한과 쓰는 곳",
     [["사진: 새 스크린샷을 감지하고 담아 둔 사진을 보여 주기 위해",
       "알림: 캡처 직후 폴더 고르기, 날짜 알림, 감지 상태 표시를 위해",
       "다른 앱 위에 표시(선택): 캡처 직후 화면 구석에 폴더 버튼을 띄우기 위해",
       "카메라: 앱 안에서 기록 사진을 찍기 위해",
       "마이크: 요리 모드에서 \"다음\", \"다시\" 같은 짧은 음성 명령을 알아듣기 위해",
       "미디어 관리: 이용자가 \"갤러리에서 삭제\"를 고른 사진을 휴대폰 휴지통으로 옮기기 위해",
       "그 밖에 진동, 재부팅 후 감지 다시 켜기, 백그라운드 감지 유지, 구글 플레이 결제 연결"],
      "권한은 휴대폰 설정에서 언제든 끌 수 있습니다. 끈 권한과 관련된 기능만 멈추고 나머지는 계속 쓸 수 있습니다."]),
    ("5. 이용자가 직접 밖으로 보내는 경우",
     ["다음은 이용자가 직접 고를 때만 일어나며, 받는 쪽 서비스의 정책이 적용됩니다.",
      ["공유: 이용자가 고른 앱으로 사진이 전달됩니다.",
       "지도에서 열기: 장소 이름이 이용자가 쓰는 지도 앱으로 전달됩니다.",
       "백업 파일: 이용자가 고른 저장 위치에 파일이 만들어집니다. 그 위치가 클라우드라면 해당 서비스에 저장됩니다.",
       "개선 제안 메일: 메일 앱으로 보내면 개발자는 보낸 사람의 메일 주소와 내용, 함께 적힌 기기 정보(모델·안드로이드 버전·앱 버전)를 받고 답장에만 씁니다."]]),
    ("6. 구매",
     ["\"쏙 프로\" 구매는 구글 플레이 결제로 이루어집니다. 결제 수단 등 결제 정보는 구글이 처리하며 "
      "개발자에게 전달되지 않습니다. 앱은 구매했는지 여부만 구글 플레이를 통해 확인합니다."]),
    ("7. 보관과 삭제",
     ["앱을 삭제하면 앱 전용 공간의 기록과 앱에서 찍은 사진이 모두 함께 지워집니다. "
      "갤러리의 스크린샷 원본은 앱 삭제와 상관없이 남습니다. "
      "앱 안에서 \"갤러리에서 삭제\"를 고른 사진은 휴대폰 휴지통으로 옮겨지며, 휴지통 정책(보통 30일)에 따라 완전히 지워집니다. "
      "개발자는 이용자 데이터를 따로 보관하지 않으므로 개발자에게 삭제를 요청할 데이터가 없습니다."]),
    ("8. 아동의 개인정보",
     ["앱은 만 14세 미만 아동을 대상으로 하지 않습니다."]),
    ("9. 문의",
     [f"개인정보 처리에 관한 문의는 {CONTACT} 로 보내 주세요."]),
    ("10. 방침 변경",
     ["내용이 바뀌면 이 페이지의 시행일을 갱신하고, 중요한 변경은 앱 업데이트 안내에 함께 적습니다."]),
]

PRIVACY_EN = [
    ("1. Summary",
     ["ssok (the \"App\") organizes screenshots and photo notes on your phone. The App has no internet "
      "permission. Your photos and records never leave your phone through the App, and the developer cannot "
      "see them. There is no sign-up, no login, no advertising and no analytics."]),
    ("2. What the App handles and where it is stored",
     ["Everything is stored only in the App's private storage on your phone.",
      ["Filing records: which screenshot went to which folder, dates and place names you set, and whether an item is finished",
       "Text read from photos: part of the text recognized on the device, used for search and date suggestions",
       "Photos taken in the App: photo notes taken with the in-app camera (not saved to the gallery)",
       "Settings: folder names and order, reminder timing, display language and so on"],
      "Original screenshots stay in your gallery. The App never copies or moves them; it only remembers where they are."]),
    ("3. Processed on the device only",
     [["Text and barcode recognition uses an on-device model.",
       "Read-aloud uses your phone's text-to-speech engine.",
       "Voice commands (cooking mode) use on-device speech recognition only. If your device does not support it, voice commands stay off."]]),
    ("4. Permissions and why",
     [["Photos: to detect new screenshots and show the photos you saved",
       "Notifications: to pick a folder right after a capture, for date reminders and to show detection status",
       "Display over other apps (optional): to show folder buttons in a corner right after a capture",
       "Camera: to take photo notes inside the App",
       "Microphone: to understand short voice commands such as \"next\" or \"again\" in cooking mode",
       "Media management: to move photos you chose to delete from the gallery into your phone's trash",
       "Also: vibration, restarting detection after reboot, keeping detection running, Google Play billing"],
      "You can turn permissions off at any time in your phone settings. Only the related feature stops."]),
    ("5. When you send something out yourself",
     ["These happen only when you choose them, and the receiving service's policy applies.",
      ["Share: the photo goes to the app you pick.",
       "Open in maps: the place name goes to your map app.",
       "Backup file: a file is created at the location you pick. If that location is a cloud service, the file is stored there.",
       "Feedback email: if you send it, the developer receives your email address, the message and the device details included (model, Android version, app version), used only to reply."]]),
    ("6. Purchases",
     ["\"ssok Pro\" is purchased through Google Play billing. Payment details are handled by Google and are "
      "not shared with the developer. The App only checks with Google Play whether you have purchased it."]),
    ("7. Retention and deletion",
     ["Uninstalling the App deletes all records in its private storage, including photos taken in the App. "
      "Original screenshots in your gallery remain. Photos you choose to \"Delete from gallery\" are moved to "
      "your phone's trash and are removed according to its policy (usually 30 days). The developer keeps no "
      "copy of your data, so there is nothing to request deletion of from the developer."]),
    ("8. Children",
     ["The App is not directed to children under 14."]),
    ("9. Contact",
     [f"Questions about privacy: {CONTACT}"]),
    ("10. Changes",
     ["If this policy changes, the effective date on this page is updated. Important changes are also noted in app update notes."]),
]

# ── 이용약관 ─────────────────────────────────────────────────────────

TERMS_KO = [
    ("1. 목적",
     ["이 약관은 쏙(이하 \"앱\")을 이용하는 데 필요한 사항을 정합니다. 앱을 설치해 사용하면 이 약관에 동의한 것으로 봅니다."]),
    ("2. 서비스 내용",
     ["앱은 이용자의 휴대폰 안에서 스크린샷을 폴더로 정리하고, 날짜 알림·검색·요리 모드·사진 기록 같은 기능을 제공하는 도구입니다. "
      "별도 서버나 계정 없이 휴대폰 안에서만 동작합니다."]),
    ("3. 무료 체험과 쏙 프로",
     [["앱을 처음 설치한 날부터 30일 동안 모든 기능을 무료로 쓸 수 있습니다.",
       "체험이 끝나면 새 캡처 담기와 새 기록 시작만 멈춥니다. 이미 담은 것은 계속 열고, 꺼내 쓰고, 끝내고, 삭제할 수 있습니다.",
       "\"쏙 프로\"를 한 번 구매하면 새로 담기를 계속 쓸 수 있습니다. 구독이 아니며 추가 결제가 없습니다.",
       "구매는 구매에 쓴 구글 계정에 기록되어, 같은 계정으로 다시 설치하면 \"구매 내역 다시 불러오기\"로 되살릴 수 있습니다.",
       "결제와 환불은 구글 플레이의 정책과 절차를 따릅니다."]]),
    ("4. 인식 결과와 알림의 한계",
     ["사진에서 읽은 날짜·장소 이름·재료와 조리 순서는 자동 인식이라 틀릴 수 있습니다. 앱은 확정 전에 이용자에게 확인을 묻지만, "
      "쿠폰 만료일이나 예약 날짜 같은 중요한 정보는 원본에서 직접 확인해 주세요. "
      "알림은 휴대폰의 절전·알림 설정에 따라 늦거나 오지 않을 수 있습니다."]),
    ("5. 사진 기록의 성격",
     ["앱에서 찍은 사진에 표시되는 시각과 기록은 이용자의 기억을 돕기 위한 것이며, 법적 증거로서의 효력을 보장하지 않습니다."]),
    ("6. 이용자의 책임",
     [["이용자가 \"갤러리에서 삭제\"를 고르면 원본이 휴대폰 휴지통으로 옮겨집니다. 휴지통을 비우면 되살릴 수 없습니다.",
       "앱에서 찍은 사진은 앱 전용 공간에 있어 앱을 삭제하면 함께 지워집니다. 남겨야 할 것은 미리 공유하거나 백업 파일로 내보내 주세요.",
       "휴대폰을 바꿀 때는 설정의 \"폰을 바꿀 때\"에서 백업 파일을 만들어 옮겨 주세요."]]),
    ("7. 책임의 제한",
     ["법령이 허용하는 범위에서, 앱 이용 중 생긴 데이터 손실이나 인식·알림 오류로 인한 손해에 대해 개발자는 책임을 지지 않습니다. "
      "다만 개발자의 고의 또는 중대한 과실로 생긴 손해는 예외입니다."]),
    ("8. 서비스 변경",
     ["기능은 앱 업데이트로 바뀔 수 있습니다. 이미 구매한 \"쏙 프로\"의 혜택(새로 담기)은 줄이지 않습니다."]),
    ("9. 문의",
     [f"약관에 관한 문의는 {CONTACT} 로 보내 주세요."]),
]

TERMS_EN = [
    ("1. Purpose",
     ["These terms govern your use of ssok (the \"App\"). By installing and using the App you agree to them."]),
    ("2. The service",
     ["The App organizes screenshots into folders on your phone and offers date reminders, search, cooking mode and "
      "photo notes. It works on your phone only, with no server and no account."]),
    ("3. Free trial and ssok Pro",
     [["All features are free for 30 days from the day you first install the App.",
       "After the trial, only adding new captures and starting new records stops. You can still open, use, finish and delete what you already saved.",
       "A one-time purchase of \"ssok Pro\" keeps adding new items available. It is not a subscription and there are no further charges.",
       "The purchase is tied to the Google account used to buy it. Reinstall with the same account and use \"Restore purchase\".",
       "Payments and refunds follow Google Play's policies and procedures."]]),
    ("4. Limits of recognition and reminders",
     ["Dates, place names, ingredients and recipe steps read from photos are recognized automatically and can be wrong. "
      "The App asks you to confirm them, but please check important details such as coupon expiry or booking dates in the original. "
      "Reminders may be late or missing depending on your phone's battery and notification settings."]),
    ("5. Nature of photo notes",
     ["Times and notes shown on photos taken in the App are there to help you remember. They are not guaranteed to have any legal effect as evidence."]),
    ("6. Your responsibilities",
     [["If you choose \"Delete from gallery\", the original is moved to your phone's trash. Once the trash is emptied it cannot be restored.",
       "Photos taken in the App live in its private storage and are deleted when the App is uninstalled. Share or export a backup file first if you need to keep them.",
       "When changing phones, create a backup file under \"Switching phones\" in Settings and import it on the new phone."]]),
    ("7. Limitation of liability",
     ["To the extent permitted by law, the developer is not liable for data loss or for damage caused by recognition or reminder errors, "
      "except where caused by the developer's intent or gross negligence."]),
    ("8. Changes",
     ["Features may change through app updates. The benefit of an already purchased \"ssok Pro\" (adding new items) will not be reduced."]),
    ("9. Contact",
     [f"Questions about these terms: {CONTACT}"]),
]


def esc(s):
    return html.escape(s, quote=False)


def body(sections):
    out = []
    for title, parts in sections:
        out.append(f"<h2>{esc(title)}</h2>")
        for p in parts:
            if isinstance(p, list):
                out.append("<ul>" + "".join(f"<li>{esc(i)}</li>" for i in p) + "</ul>")
            else:
                out.append(f"<p>{esc(p)}</p>")
    return "\n".join(out)


def nav(current):
    items = [("index.html", "홈 · Home"), ("privacy.html", "개인정보 처리방침 · Privacy"), ("terms.html", "이용약관 · Terms")]
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
<footer>문의 · Contact <a href="mailto:{CONTACT}">{CONTACT}</a></footer>
</div></body>
</html>
"""
    (OUT / file).write_text(doc, encoding="utf-8")


def legal(file, ko_title, en_title, ko, en):
    page(file, f"{ko_title} · {APP_KO}", f"""
<h1>{esc(ko_title)}</h1>
<p class="meta">{APP_KO} · 시행일 {EFFECTIVE_KO} · <a href="#en">English</a></p>
{body(ko)}
<div class="lang" id="en">
<h1>{esc(en_title)}</h1>
<p class="meta">{APP_EN} · Effective {EFFECTIVE_EN}</p>
{body(en)}
</div>""")


page("index.html", f"{APP_KO} · {APP_EN}", f"""
<h1>{esc(APP_KO)}</h1>
<p class="meta">Google Play: {esc(PLAY_NAME_KO)} / {esc(PLAY_NAME_EN)}</p>
<p>나중에 쓸 스크린샷을 폴더에 쏙 모으고, 주차 위치와 사진 기록을 남기는 안드로이드 앱이에요. 인터넷 권한이 없어 사진이 휴대폰 밖으로 나가지 않아요.</p>
<p>An Android app that collects screenshots you will use later into folders and keeps photo notes such as where you parked. It has no internet permission, so your photos never leave your phone.</p>
<ul>
<li><a href="privacy.html">개인정보 처리방침 · Privacy Policy</a></li>
<li><a href="terms.html">이용약관 · Terms of Use</a></li>
</ul>""")

legal("privacy.html", "개인정보 처리방침", "Privacy Policy", PRIVACY_KO, PRIVACY_EN)
legal("terms.html", "이용약관", "Terms of Use", TERMS_KO, TERMS_EN)
print("ok")
