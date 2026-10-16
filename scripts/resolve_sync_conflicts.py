import os
import re

def resolve_all():
    # 1. app/build.gradle.kts
    gradle_file = "app/build.gradle.kts"
    if os.path.exists(gradle_file):
        with open(gradle_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        conflict_pattern = re.compile(
            r'<<<<<<< HEAD\s+versionCode\s*=\s*(\d+)\s+versionName\s*=\s*"([^"]+)"\s+=======\s+versionCode\s*=\s*(\d+)\s+versionName\s*=\s*"([^"]+)"\s+>>>>>>> [^\n]+',
            re.MULTILINE
        )
        def fix_version(match):
            head_code = int(match.group(1))
            head_name = match.group(2)
            up_code = int(match.group(3))
            new_code = max(head_code, up_code) + 1
            parts = head_name.split(".")
            try:
                parts[-1] = str(int(parts[-1]) + 1)
                new_name = ".".join(parts)
            except Exception:
                new_name = f"{head_name}.1"
            return f'        versionCode = {new_code}\n        versionName = "{new_name}"'
        
        content = conflict_pattern.sub(fix_version, content)
        content = content.replace('"NuvioMedia"', '"AlessandroA586"')
        with open(gradle_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Processed build.gradle.kts")

    # 2. app/src/main/res/values-it/strings.xml
    it_strings = "app/src/main/res/values-it/strings.xml"
    if os.path.exists(it_strings):
        with open(it_strings, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        conflict_pattern = re.compile(
            r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> [^\n]+\n',
            re.DOTALL
        )
        match = conflict_pattern.search(content)
        if match:
            head_part = match.group(1)
            content = content.replace(match.group(0), head_part + "\n")
        content = content.replace("l\\'RPU", "l'RPU").replace("dell\\'opzione", "dell'opzione")
        with open(it_strings, "w", encoding="utf-8") as f:
            f.write(content)
        print("Processed values-it/strings.xml")

    # 3. StreamAutoPlaySelector.kt
    auto_file = "app/src/main/java/com/nuvio/tv/core/player/StreamAutoPlaySelector.kt"
    if os.path.exists(auto_file):
        with open(auto_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        new_lines = [line for line in lines if "append(stream.getStreamUrl().orEmpty())" not in line]
        with open(auto_file, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Processed StreamAutoPlaySelector.kt")

    # 4. AboutScreen.kt
    about_file = "app/src/main/java/com/nuvio/tv/ui/screens/settings/AboutScreen.kt"
    if os.path.exists(about_file):
        with open(about_file, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace(
            "stringResource(R.string.about_version, BuildConfig.VERSION_NAME)",
            '"Juansher | V${BuildConfig.VERSION_NAME}"'
        )
        with open(about_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Processed AboutScreen.kt")

if __name__ == "__main__":
    resolve_all()
