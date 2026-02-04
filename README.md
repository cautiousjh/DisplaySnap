# Multi Monitor Config

Windows용 모니터 설정 관리 도구. 시스템 트레이에서 저장된 프로필로 빠르게 모니터 설정을 전환할 수 있습니다.

## 기능

- **프로필 저장/로드**: 현재 모니터 설정을 프로필로 저장하고 클릭 한 번으로 복원
- **모니터 Enable/Disable**: 특정 모니터를 비활성화하는 설정도 저장 가능
- **자동 감지**: 비활성화된 모니터도 프로필 적용 시 자동으로 다시 활성화
- **시스템 트레이**: 트레이 아이콘에서 빠르게 프로필 전환
- **Export/Import**: 프로필을 JSON 파일로 내보내기/가져오기

## 설치

### 방법 1: Python으로 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# 실행
python main.py
# 또는
run.bat
```

### 방법 2: exe 파일 사용

[Releases](../../releases) 페이지에서 `MultiMonitorConfig.exe` 다운로드 후 실행

## 사용법

1. 트레이 아이콘 더블클릭 → 설정 창 열기
2. **Save** 버튼으로 현재 모니터 설정 저장
3. 프로필 선택 후 **Apply** 또는 더블클릭으로 적용
4. 트레이 메뉴에서도 프로필 바로 적용 가능

### 모니터 비활성화

- Current Monitors에서 체크 해제 후 Save → 해당 모니터 disabled로 저장
- "Disable monitors not in profile" 옵션 체크 시 → 프로필에 없는 모니터 자동 비활성화

## 저장 위치

프로필은 `%AppData%\MultiMonitorConfig\profiles.json`에 저장됩니다.

## 빌드

```bash
# PyInstaller 설치
pip install pyinstaller

# exe 빌드
build.bat
```

→ `dist/MultiMonitorConfig.exe` 생성

## 기술 스택

- Python 3.7+
- customtkinter (UI)
- pystray (시스템 트레이)
- Windows API (EnumDisplayDevices, ChangeDisplaySettingsEx, SetDisplayConfig)

## 스크린샷

```
┌─────────────────────────────────────┐
│ Current Monitors                    │
│   [✓] \\.\DISPLAY1: 2560x1440 @ 59Hz│
│   [✓] \\.\DISPLAY2: 1920x1080 @ 60Hz│
├─────────────────────────────────────┤
│ Saved Profiles                      │
│   ┌─────────────────────────────┐   │
│   │ 🖥️ Dual Setup               │   │
│   │ 🖥️ Single Monitor           │   │
│   │ 🖥️ Portable                 │   │
│   └─────────────────────────────┘   │
├─────────────────────────────────────┤
│ Profile Detail                      │
│   [enabled] \\.\DISPLAY1: 2560x1440 │
├─────────────────────────────────────┤
│ [✓] Disable monitors not in profile │
├─────────────────────────────────────┤
│ [Save][Apply][Rename][Delete] ↑↓ ↻  │
└─────────────────────────────────────┘
```

## License

MIT
