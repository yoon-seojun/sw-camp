import math
def sphere_area(diameter, material="glass", thickness=1):
    """
    지름이 diameter인 반구의 겉넓이를 반환합니다.
    (바닥면 포함)
    material: 'glass', 'aluminum', 'carbon_steel' 중 하나 (기본값: 'glass')
    thickness: 두께(cm) (기본값: 1)
    무게 계산에는 사용하지 않음 (겉넓이만 반환)
    """
    r = diameter / 2
    area = 3 * math.pi * r**2
    return area
print(sphere_area(10))

def sphere_area_with_weight(diameter, material, thickness):
    """
    지름이 diameter인 반구의 겉넓이(㎡)와 질량(kg), 지구/화성 중력 기준 무게(N)를 반환합니다.
    material: 'glass', 'aluminum', 'carbon_steel' 중 하나
    thickness: 두께(cm)
    (바닥면 포함)
    """
    densities = {
        'glass': 2.4,
        'aluminum': 2.7,
        'carbon_steel': 7.85
    }
    r = diameter / 2
    area_m2 = 3 * math.pi * r**2  # m²
    area_cm2 = area_m2 * 10000    # 1m² = 10,000cm²
    density = densities.get(material)
    if density is None:
        raise ValueError('지원하지 않는 재질입니다.')
    weight_g = area_cm2 * thickness * density
    mass_kg = weight_g / 1000
    weight_earth = mass_kg * 9.80665
    weight_mars = mass_kg * 3.72076
    return area_m2, mass_kg, weight_earth, weight_mars

# 전역변수 선언
material = None
diameter = None
thickness = None
area = None
weight = None

# 예시 출력
material, diameter, thickness = 'glass', 10, 1
area, mass, w_earth, w_mars = sphere_area_with_weight(diameter, material, thickness)
weight = mass  # 질량(kg) 기준
print(f"재질 =⇒ 유리, 지름 =⇒ {diameter:.3f}, 두께 =⇒ {thickness:.3f}, 면적 =⇒ {area:.3f}, 무게 =⇒ {weight:.3f} kg")

# 사용자 입력 받기
try:
    diameter = float(input("돔의 지름을 입력하세요(m): "))
    material = input("재질을 입력하세요 (glass/aluminum/carbon_steel): ").strip().lower()
    thickness = float(input("두께를 입력하세요(cm): "))
    area, mass, w_earth, w_mars = sphere_area_with_weight(diameter, material, thickness)
    weight = mass
    material_kor = {'glass': '유리', 'aluminum': '알루미늄', 'carbon_steel': '탄소강'}.get(material, material)
    print(f"재질 =⇒ {material_kor}, 지름 =⇒ {diameter:.3f}, 두께 =⇒ {thickness:.3f}, 면적 =⇒ {area:.3f}, 무게 =⇒ {weight:.3f} kg")
except Exception as e:
    print("오류:", e)
