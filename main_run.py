import folium
from folium import plugins

# 1. רשימת הזכרונות - כאן שמתי דוגמה עם מחרוזת ריקה בשורה השנייה
memories = [
    [32.0853, 34.7818, "הדייט הראשון", "כאן הכל התחיל...", "https://via.placeholder.com/150"],
    [32.1643, 34.8447, "הנשיקה הראשונה", "רגע שלא אשכח.", ""], # סטרינג ריק - לא תוצג תמונה
    [32.9812, 35.5123, "חגיגות חצי שנה", "התחנה הבאה שלנו!", None],
    [32.119177, 34.821454,"ממסאג' לנשיקה", "היה מסאג' נחמד אבל לדעתי הנשיקה הייתה הרבה יותר שווה",None],
    [32.12301749051284, 34.796344793133535,"הבית שלךךךךך", "מאוד כיף בבית שלך מאמי",None]

]

# 2. יצירת המפה
m = folium.Map(location=[32.5, 34.8], zoom_start=8, tiles='CartoDB positron')

# 3. הוספת הנקודות למפה
for lat, lon, title, description, img_url in memories:
    
    # בדיקה: אם הסטרינג של התמונה קיים ואינו ריק
    img_tag = ""
    if img_url and img_url.strip():
        img_tag = f'<img src="{img_url}" alt="{title}" style="width:100%; border-radius: 5px; margin-bottom: 5px;">'
    
    # בניית ה-HTML - ה-img_tag ייכנס רק אם הוא נוצר
    html = f"""
    <div style="font-family: 'Arial', sans-serif; direction: rtl; text-align: right; width: 200px;">
        <h4 style="margin-bottom: 5px; color: #e63946;">{title}</h4>
        {img_tag}
        <p style="font-size: 13px; line-height: 1.4;">{description}</p>
        <hr style="border: 0.5px solid #eee;">
        <p style="font-size: 11px; color: gray;">קואורדינטות: {lat}, {lon}</p>
    </div>
    """
    
    popup = folium.Popup(html, max_width=250)
    folium.Marker(
        [lat, lon],
        popup=popup,
        icon=folium.Icon(color='red', icon='heart', prefix='fa'),
        tooltip=title
    ).add_to(m)

# 4. שמירה כ-index.html כדי ש-GitHub Pages יזהה אותו
m.save("index.html")
print("הקוד עודכן! כעת תמונות ריקות לא יופיעו כסימן שבור.")