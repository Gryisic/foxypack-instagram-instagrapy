import pandas as pd
from foxypack import FoxyPack
from foxypack.entitys.balancers import BaseEntityBalancer
from foxypack.entitys.pool import EntityPool
from foxypack_instagram_instagrapy import (
    InstagramAccount,
    FoxyInstagramAnalysis,
    FoxyInstagramStat,
)

# Инициализация аккаунта Instagram
instagram_account = InstagramAccount(
    login_account="shapranov.work@gmail.com",
    password="15426378ShapDi",
    path_session_file="session_account_instagram.json",
)
print(instagram_account)

# Инициализация пула и парсера
pool = EntityPool(path="str.json")
entity_balancer = BaseEntityBalancer(pool=pool)
pool.add(instagram_account)

parser = (
    FoxyPack()
    .with_foxy_analysis(FoxyInstagramAnalysis())
    .with_foxy_stat(
        FoxyInstagramStat(entity_balancer=entity_balancer, entity_pool=pool)
    )
)

# Список Instagram ссылок (замените на ваши реальные ссылки)
instagram_links = [
    "https://www.instagram.com/reel/DPWT_T8DMLe/?igsh=MTllNzhhdnNib3Zpag==",
    "https://www.instagram.com/reel/DPeRKS6kd12/?igsh=YWNuZmJndjhkbWZm",
    "https://www.instagram.com/reel/DPeS5wjDjIi/?igsh=NXBzMGlrbDljZDJ0",
    "https://www.instagram.com/reel/DPilsoEgVMA/?igsh=MWt4b2VnMzhnNG5oYQ==",
    "https://www.instagram.com/reel/DPlyNsIDL8x/?igsh=eDdpeGl5NnJ6em1o",
    "https://www.instagram.com/reel/DPnd2x-kxkM/?igsh=bWdieWV3ZjN6eGNn",
    "https://www.instagram.com/reel/DPn83MZkYNy/?igsh=MThjM2hzYWsyaGJkNA==",
    "https://www.instagram.com/reel/DPqO90jDdU5/?igsh=MTV2b2Y1eGt0aXh5NA==",
    "https://www.instagram.com/reel/DPtSr56E417/?igsh=aThqYTYxZ3Y0bm4z",
    "https://www.instagram.com/reel/DPv889Mj9CF/?igsh=cmF0OTR1MXJobWU4",
    "https://www.instagram.com/reel/DPv9f2mkW48/?igsh=YXpnZmIzNHE3cDU%3D",
    "https://www.instagram.com/stories/a.v.a.n.ii.__/3742477995341761335?utm_source=ig_story_item_share&igsh=ZnJ3dTUzcmhnOW82",
    "https://www.instagram.com/stories/a.v.a.n.ii.__/3742481732198150642?utm_source=ig_story_item_share&igsh=MXE2c2VqbjJyMWN5Ng==",
    "https://www.instagram.com/reel/DPwGF9wEviL/?igsh=MTl4eW5uYWV4Yjc2Mw==",
    "https://www.instagram.com/reel/DPwMntLDAWN/?igsh=MThybTlmaGVnMjFhaA%3D%3D",
    "https://www.instagram.com/reel/DPwNKMfE8dy/?igsh=N2hyb29ka2Y1dzg1",
    "https://www.instagram.com/reel/DPv_rnoCt4c/?igsh=MXU2bWozbTdveHJxeQ==",
    "https://www.instagram.com/reel/DPx70u3EhoP/?igsh=MTg2ZTF3Z210bDdqdQ%3D%3D",
    "https://www.instagram.com/reel/DPyE_Cnj6PA/?igsh=MmJqMXA4YndwZDly",
    "https://www.instagram.com/reel/DP07aA_EhY0/?igsh=bHBoMWtvdm54NThw",
    "https://www.instagram.com/reel/DP1PMk-E30Y/?igsh=MTd1dGoycjd6N2t6YQ%3D%3D",
    "https://www.instagram.com/reel/DP3ukBLEg86/?igsh=MWwzZWR5cGZkZjdteA%3D%3D",
    "https://www.instagram.com/reel/DP5nNxskgcv/?igsh=MWJ6ZHpvOWF6dGFwdA%3D%3D",
    "https://www.instagram.com/reel/DP50g3uEiYf/?igsh=MWkycTcydDEyOTJkdw==",
    "https://www.instagram.com/reel/DP8Q_btgbee/?igsh=MW55cjA5N2U2ODd2MA==",
    "https://www.instagram.com/reel/DP8cSsjkcjU/?igsh=MXBqbWt5amo4MXYwZQ==",
    "https://www.instagram.com/reel/DP6OlLYE9z0/?igsh=Z9p6d2jzdHV3NG77",
    "https://www.instagram.com/stories/a.v.a.n.ii.__/374247099534176169?utm_source=ig_story_item_share&amp",
    "https://www.instagram.com/stories/a.v.a.n.ii.__/3742481732199178552?utm_source=ig_story_item_share&amp;igsh=MXE2c2VqbjJyMWN5Ng==",
    "https://www.instagram.com/reel/DQGT0Ebj9uf/?igsh=NnNjcnFyY3RiN2J3",
    "https://www.instagram.com/reel/DQGUQUzEswI/?igsh=MTQ4Z3R4cGc3MjlyZA%3D%3D",
    "https://www.instagram.com/reel/DQGWnjXj2Ls/?igsh=ZnZ0MWY1eXgwbzZr",
    "https://www.instagram.com/reel/DQGbaFNEYPT/",
    "https://www.instagram.com/reel/DQGeX8TEkvW/",
    "https://www.instagram.com/reel/DQGkW0xkyVY/?igsh=cW4zcjM0Ym55Nm1p",
    "https://www.instagram.com/reel/DQGkTMSCbzj/?igsh=eTUyNTh5YWhlZmxr",
    "https://www.instagram.com/reel/DQGktkdCXlC/?igsh=bHdsNGozaDZpb2ti",
    "https://www.instagram.com/reel/DQGm705kY_N/?igsh=bDY2Nmpvc3pwY3U2",
    "https://www.instagram.com/reel/DQGovRzEbnh/?igsh=MWtvNXZ0eTNsOGZnNw%3D%3D",
    "https://www.instagram.com/reel/DQGskOkj0fa/?igsh=MTF5b211OTJoYXlwMg==",
    "https://www.instagram.com/reel/DPAtSa6EW74/?igsh=OWpwd3R6NWF1cmU4",
    "https://www.instagram.com/reel/DPTfNqgEbI3/?igsh=MTl1dDAzd2VwNTdyYw%3D%3D",
    "https://www.instagram.com/reel/DPTPq7Kj0tO/?igsh=MTU4Mjd4eWs4MW5hZg%3D%3D",
    "https://drive.google.com/file/d/1pkRQjRnEZR_Ve9jPA8koSHMg4KaFxTVO/view?usp=sharing",
    "https://www.instagram.com/reel/DPfhw-eExd1/?igsh=eGpvZW9udDZ5d3dh",
    "https://www.instagram.com/reel/DPiWg2ekQhL/?igsh=NHZucWlpbzM0eW5r",
    "https://www.instagram.com/reel/DPh-Bx9Eu5R/?igsh=MWx4NDJxZmE5eXNsaA%3D%3D",
    "https://www.instagram.com/reel/DPn1WsVk1yi/?igsh=MXRnYzVtc3J3dGpkZg%3D%3D",
    "https://www.instagram.com/reel/DPn4lMlkn0G/?igsh=MXhnMTUxeDQ4YWQwdA%3D%3D",
    "https://www.instagram.com/reel/DPnxm5HEZeZ/?igsh=Y3h0NmNwZXU4N3Bh",
    "https://www.instagram.com/reel/DPnfcejEh96/?igsh=bWRxaDNtNTF4b3V6",
    "https://www.instagram.com/reel/DPnfuGuD2Nm/?igsh=MTh5am02bm1tNm04bg%3D%3D",
    "https://www.instagram.com/reel/DPnkRMEERFo/?igsh=MWZhdnk5cTM3NzhpNg%3D%3D",
    "https://www.instagram.com/reel/DPQ_zDuD7gs/?igsh=dzhwcnc4YnhuOWl1",
    "https://www.instagram.com/reel/DPvwHyIEnQB/?igsh=MTExbmdhNTk3OHFocg%3D%3D",
    "https://www.instagram.com/reel/DP4emdmE2CX/?igsh=MXN0aXJzdnhnazRvMg%3D%3D",
    "https://www.instagram.com/reel/DP5otUbEV8K/?igsh=MTF6dWEyc2FpamEycw%3D%3D",
    "https://www.instagram.com/reel/DQBQQfKDMct/?igsh=aTRqZWhxZ3dqZzI3",
    "https://www.instagram.com/reel/DQBv2eKkdzH/?igsh=dmhoeTgyYjVmaHRl",
    "https://www.instagram.com/reel/DQCGS3vEozr/?igsh=ZGMxN2ljYXlrZWNw",
    "https://www.instagram.com/reel/DQCDXLcgV6L/?igsh=c3ZpN2RkY3VtcDli",
    "https://www.instagram.com/ranjan_vermaa/",
    "https://www.instagram.com/reel/DQEJFv_k297/?igsh=MWkwODZiYmE5ZWhwag==",
    "https://www.instagram.com/reel/DQD2cNDgHV_/?igsh=MXdyaGllZ3Vza2Fm",
    "https://www.instagram.com/reel/DQGSoTJAT5N/?igsh=c2d4ajRlcDNyY2Qy",
    "https://www.instagram.com/reel/DPd4eHvDRsp/?igsh=MThxNTZvZGU1cTdnZw%3D%3D",
    "https://www.instagram.com/reel/DPdv8jekxYl/?igsh=MWMwaTRpOTdjMnZ0Mg%3D%3D",
    "https://www.instagram.com/reel/DPeOUh3DMF8/?igsh=MWZjNW9sYTh6cnJ3cg%3D%3D",
    "https://www.instagram.com/reel/DPYW02Egf26/?igsh=X3J2VkdvOTlN",
    "https://www.instagram.com/reel/DPeEZclE3iz/?igsh=cDFqb2dqMjNsYzQ0",
    "https://www.instagram.com/reel/DPeFdAkj0yA/?igsh=MXAzazVubHY4N3Z2bA%3D%3D",
    "https://www.instagram.com/reel/DPeFdAkj0yA/?igsh=MXAzazVubHY4N3Z2bA%3D%3D",
    "https://www.instagram.com/reel/DPeKgD9D0IN/?igsh=MWI1dWFyNjMxMjh1Ng==",
    "https://www.instagram.com/reel/DPd92mnD4Cy/?igsh=MTVqMTFmZ3M2aDRncg%3D%3D",
    "https://www.instagram.com/reel/DPifA8JEwwO/?igsh=MTFtOW9yaGRlZW1ybA%3D%3D",
    "https://www.instagram.com/reel/DPisOSMk17O/?igsh=N3NwdmwzaGw5bHc2",
    "https://www.instagram.com/reel/DPl8yxkj0GO/?igsh=MjN1ZjdkZ256dDRw",
    "https://www.instagram.com/reel/DPi4OSpkcL1/?igsh=aDBlY3IyMDU2cHow",
    "https://www.instagram.com/reel/DPlj6jnkj80/?igsh=MTltb2Q3dGpzam83cQ%3D%3D",
    "https://www.instagram.com/reel/DPjSo5Zko0J/",
    "https://www.instagram.com/reel/DPyu5f6Alpq/?igsh=ZGZzdzhpb3h4azdn",
    "https://www.instagram.com/reel/DP6Xc-SCCEI/?igsh=eTd4cTc5MDZnYmhk",
    "https://www.instagram.com/reel/DP6ra9GEqlK/?igsh=MWZ6cmpsMXpnbDM5aA==",
    "https://www.instagram.com/reel/DQBAQuWjynj/?igsh=M2pjYTF4aGlwMmo1",
    "https://www.instagram.com/reel/DP8eAiZCc7F/?igsh=MW5yZWx2bDg0aXMwOQ==",
    "https://www.instagram.com/reel/DQEG2egifzX/?igsh=MzRyd2h6c3YxeXFo",
    "https://www.instagram.com/reel/DP06orUkpOv/?igsh=ajFoNWVsNGwzN3k5",
    "https://www.instagram.com/reel/DP8B6fzDzZ4/?igsh=M3EwZ25wN2dvN3Y%3D",
    "https://www.instagram.com/reel/DPl8yxkj0GO/?igsh=MjN1ZjdkZ256dDRw",
    "https://www.instagram.com/reel/DP_UzzkkqXC/?igsh=N3hyanpqbGZ1aHVn",
    "https://www.instagram.com/reel/DP8r3h9EnNy/?igsh=MTMyczNlZHllNWgyeQ==",
    "https://www.instagram.com/reel/DQI-SqGE5bZ/?igsh=MWVpZ2hiNWY5d3BuZw%3D%3D",
    "https://www.instagram.com/reel/DPRDvuxifnT/?igsh=MThrY24yN25rYnA2dA==",
    "https://www.instagram.com/reel/DPRD_UCkzLs/?igsh=eTV1eDZ3NTJheHJj",
    "https://www.instagram.com/reel/DPePhdqEbMq/?igsh=MTFwcTJiNW5jbXU0Zw%3D%3D",
    "https://www.instagram.com/reel/DPePxiokWMo/?igsh=MTVxd3hheWFkamZ2aA%3D%3D",
    "https://www.instagram.com/reel/DPeQmElk9On/?igsh=MWUwem5xYjg1Zm93cQ%3D%3D",
    "https://www.instagram.com/reel/DPg2zpcEwsk/?igsh=MW10emNlMnk1ZHQwdg%3D%3D",
    "https://www.instagram.com/reel/DPgx4pokyuX/?igsh=dHVpdHZqeTAzazlp",
    "https://www.instagram.com/kpf_comedy121/",
    "https://www.instagram.com/reel/DPlCEJNAaNB/?igsh=Z3RxN2k4YjNuenlw",
    "https://www.instagram.com/reel/DP5gcFijGCk/",
    "https://www.instagram.com/reel/DP5_NW0kfOy/?igsh=MWNqanlxOGRhbjVybg%3D%3D",
    "https://www.instagram.com/reel/DP9MrzAEx8c/?igsh=ZmtsajN1ZjZ4a2Jr",
    "https://www.instagram.com/reel/DP9NsjzEzCO/?igsh=MTYxbWdjdjMycGppOA%3D%3D",
    "https://www.instagram.com/reel/DP9N03IiaQN/?igsh=MWI5aG9yYnEyNmUxOQ%3D%3D",
]

# Список для хранения результатов
results = []

print("Начинаем сбор статистики Instagram...")
print(f"Используется аккаунт: {instagram_account.login_account}")

# Обработка каждой ссылки
for i, link in enumerate(instagram_links, 1):
    try:
        print(f"Обрабатывается ссылка {i}/{len(instagram_links)}: {link}")

        # Получаем статистику для текущей ссылки Instagram
        data = parser.get_statistics(link)
        print(data)
        # Извлекаем данные согласно структуре ответа
        answer_id = getattr(data, "answer_id", "N/A")
        pk = getattr(data, "pk", "N/A")
        instagram_id = getattr(data, "instagram_id", "N/A")
        view_count = getattr(data, "view_count", 0)
        video_duration = getattr(data, "video_duration", 0)
        like_count = getattr(data, "like_count", 0)
        play_count = getattr(data, "play_count", 0)
        caption_text = getattr(data, "caption_text", "")
        comment_count = getattr(data, "comment_count", 0)

        # Расчет вовлеченности
        engagement_rate = 0
        if play_count > 0:
            engagement_rate = round((like_count + comment_count) / play_count * 100, 2)
        elif view_count > 0:
            engagement_rate = round((like_count + comment_count) / view_count * 100, 2)

        # Добавляем результат в список
        results.append(
            {
                "url": link,
                "answer_id": answer_id,
                "pk": pk,
                "instagram_id": instagram_id,
                "view_count": view_count,
                "video_duration": video_duration,
                "like_count": like_count,
                "play_count": play_count,
                "comment_count": comment_count,
                "caption_text": caption_text[:100] + "..."
                if len(caption_text) > 100
                else caption_text,  # Обрезаем длинный текст
                "engagement_rate": engagement_rate,
                "total_engagement": like_count + comment_count,
            }
        )

        print(
            f"  ✅ Успешно: {like_count} лайков, {comment_count} комментариев, {play_count} проигрываний"
        )

    except Exception as e:
        print(f"  ❌ Ошибка при обработке {link}: {e}")
        # Добавляем запись с ошибкой
        results.append(
            {
                "url": link,
                "answer_id": f"Ошибка: {str(e)}",
                "pk": f"Ошибка: {str(e)}",
                "instagram_id": f"Ошибка: {str(e)}",
                "view_count": f"Ошибка: {str(e)}",
                "video_duration": f"Ошибка: {str(e)}",
                "like_count": f"Ошибка: {str(e)}",
                "play_count": f"Ошибка: {str(e)}",
                "comment_count": f"Ошибка: {str(e)}",
                "caption_text": f"Ошибка: {str(e)}",
                "engagement_rate": f"Ошибка: {str(e)}",
                "total_engagement": f"Ошибка: {str(e)}",
            }
        )

# Создаем DataFrame из результатов
df = pd.DataFrame(results)

# Сохраняем в Excel файл с настройками форматирования
excel_filename = "instagram_statistics_detailed.xlsx"

try:
    with pd.ExcelWriter(excel_filename, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Детальная статистика", index=False)

        # Создаем сводную таблицу для успешных результатов
        successful_results = [r for r in results if isinstance(r["like_count"], int)]
        if successful_results:
            summary_df = pd.DataFrame(successful_results)
            summary_stats = pd.DataFrame(
                {
                    "Метрика": [
                        "Всего постов",
                        "Всего лайков",
                        "Всего комментариев",
                        "Всего проигрываний",
                        "Средняя вовлеченность",
                    ],
                    "Значение": [
                        len(successful_results),
                        sum(r["like_count"] for r in successful_results),
                        sum(r["comment_count"] for r in successful_results),
                        sum(r["play_count"] for r in successful_results),
                        f"{sum(r['engagement_rate'] for r in successful_results) / len(successful_results):.2f}%",
                    ],
                }
            )
            summary_stats.to_excel(writer, sheet_name="Сводка", index=False)

    print(f"\n✅ Готово! Результаты сохранены в файл: {excel_filename}")

except Exception as e:
    print(f"❌ Ошибка при сохранении в Excel: {e}")
    # Альтернативное сохранение в CSV
    csv_filename = "instagram_statistics.csv"
    df.to_csv(csv_filename, index=False, encoding="utf-8-sig")
    print(f"✅ Результаты сохранены в CSV файл: {csv_filename}")

# Выводим итоговую статистику
successful_count = len([r for r in results if isinstance(r["like_count"], int)])
error_count = len(
    [
        r
        for r in results
        if isinstance(r["like_count"], str) and "Ошибка" in r["like_count"]
    ]
)

print(f"\n📊 ИТОГОВАЯ СТАТИСТИКА:")
print(f"✅ Успешно обработано: {successful_count}")
print(f"❌ С ошибками: {error_count}")
print(f"📝 Всего ссылок: {len(instagram_links)}")

# Детальная статистика по успешным запросам
if successful_count > 0:
    successful_results = [r for r in results if isinstance(r["like_count"], int)]
    total_likes = sum(r["like_count"] for r in successful_results)
    total_comments = sum(r["comment_count"] for r in successful_results)
    total_plays = sum(r["play_count"] for r in successful_results)
    avg_engagement = (
        sum(r["engagement_rate"] for r in successful_results) / successful_count
    )

    print(f"\n📈 СТАТИСТИКА УСПЕШНЫХ ЗАПРОСОВ:")
    print(f"❤️ Всего лайков: {total_likes}")
    print(f"💬 Всего комментариев: {total_comments}")
    print(f"▶️ Всего проигрываний: {total_plays}")
    print(f"📊 Средняя вовлеченность: {avg_engagement:.2f}%")
    print(f"🔥 Среднее количество лайков на пост: {total_likes // successful_count}")
    print(
        f"💭 Среднее количество комментариев на пост: {total_comments // successful_count}"
    )

print(f"\n🎯 Аккаунт для парсинга: {instagram_account.login_account}")
