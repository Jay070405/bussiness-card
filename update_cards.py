import sys

html_path = r'e:\2026 spring\business cards\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ================================ HTML REPLACEMENTS ================================
mesh_old = """            {
                l: '06. ABSTRACT MESH', cls: 'glass',
                f: `<div class="f-mesh c-f c">
                    <div class="mesh-glass">
                        <div class="mesh-name">Jay Lin</div>
                        <div class="mesh-title">Concept Art Director</div>
                    </div>
                </div>`,
                b: `<div class="b-mesh c-b c">
                    <div class="mesh-row" style="opacity:0.5;">CONTACT LOG_01</div>
                    <div class="mesh-row">${icoW} Wechat: ${p.v}</div>
                    <div class="mesh-row">${icoG} Web: ${p.w}</div>
                    <div class="mesh-row">${icoL} Linking: ${p.l}</div>
                </div>`
            },"""
mesh_new = """            {
                l: '06. MECHA BLUEPRINT', cls: 'matte',
                f: `<div class="f-mecha c-f c">
                    <div class="mecha-hud">
                        <div class="mecha-name">JAY LIN</div>
                        <div class="mecha-title">CONCEPT DESIGN</div>
                    </div>
                </div>`,
                b: `<div class="b-mecha c-b c">
                    <div style="font-size:16px; font-weight:800; margin-bottom:10px;">SYSTEM STATUS</div>
                    <div class="mecha-row"><span>SYS.01</span> ${icoW} ${p.v}</div>
                    <div class="mecha-row"><span>SYS.02</span> ${icoG} ${p.w}</div>
                    <div class="mecha-row"><span>SYS.03</span> ${icoL} ${p.l}</div>
                </div>`
            },"""
content = content.replace(mesh_old, mesh_new)

typo_old = """            {
                l: '11. MINIMAL TYPOGRAPHY', cls: 'matte',
                f: `<div class="f-min-typo c-f c">
                    <div class="mt-wrap">
                        <div class="mt-title">紀物</div>
                        <div class="mt-subtitle">設計</div>
                        <div class="mt-en-title">J.W DESIGN</div>
                        <div class="mt-line-vert"></div>
                        <div class="mt-line-horiz"></div>
                    </div>
                </div>`,
                b: `<div class="b-min-typo c-b c">
                    <div class="mt-b-wrap">
                        <div class="mt-b-left">
                            <div class="mt-b-name">${p.n}</div>
                            <div class="mt-b-role">${p.r}</div>
                        </div>
                        <div class="mt-b-right">
                            <div class="mt-b-row">${icoW} ${p.v}</div>
                            <div class="mt-b-row">${icoG} ${p.e}</div>
                            <div class="mt-b-row">${icoL} ${p.w}</div>
                        </div>
                    </div>
                </div>`
            },"""
typo_new = """            {
                l: '11. NEO-TOKYO TYPOGRAPHY', cls: 'matte',
                f: `<div class="f-neo-typo c-f c">
                    <div class="nt-wrap">
                        <div class="nt-title">CONCEPT</div>
                        <div class="nt-subtitle">ART</div>
                        <div class="nt-en-title">// JAY LIN LOG_01</div>
                    </div>
                </div>`,
                b: `<div class="b-neo-typo c-b c">
                    <div class="nt-b-role">// ${p.r}</div>
                    <div class="nt-b-name">${p.n}</div>
                    <div style="margin-top:20px;">
                        <div class="nt-b-row">${icoW} ${p.v}</div>
                        <div class="nt-b-row">${icoG} ${p.e}</div>
                        <div class="nt-b-row">${icoL} ${p.w}</div>
                    </div>
                </div>`
            },"""
content = content.replace(typo_old, typo_new)

obs_old = """            {
                l: '12. OBSIDIAN GLASS', cls: 'glass',
                f: `<div class="f-obs c-f c">
                    <div class="obs-glass">
                        <div class="obs-title">Jay Lin</div>
                    </div>
                </div>`,
                b: `<div class="b-obs c-b c">
                    <div class="obs-list">
                        <div class="obs-item">${icoW} ${p.v}</div>
                        <div class="obs-item">${icoG} ${p.w}</div>
                        <div class="obs-item">${icoL} ${p.l}</div>
                    </div>
                    <div class="obs-logo">JL</div>
                </div>`
            },"""
obs_new = """            {
                l: '12. DARK MATTER NEXUS', cls: 'glass',
                f: `<div class="f-dark-nexus c-f c">
                    <div class="nexus-core">
                        <div class="nexus-title">J L</div>
                    </div>
                </div>`,
                b: `<div class="b-dark-nexus c-b c">
                    <div style="font-size:24px; font-weight:800; color:#c7d2fe;">${p.n}</div>
                    <div style="font-size:10px; color:#818cf8; margin-bottom:10px;">[ ${p.r} ]</div>
                    <div class="nexus-item">${icoW} ${p.v}</div>
                    <div class="nexus-item">${icoG} ${p.w}</div>
                    <div class="nexus-item">${icoL} ${p.l}</div>
                </div>`
            },"""
content = content.replace(obs_old, obs_new)

frost_old = """            {
                l: '13. FROSTED POLYCARBONATE', cls: 'glass',
                f: `<div class="f-frost c-f c">
                    <div class="frost-txt">Jay Lin</div>
                </div>`,
                b: `<div class="b-frost c-b c">
                    <div class="frost-box">${p.r}</div>
                    <div class="frost-box">${p.e}</div>
                    <div class="frost-box">${p.w}</div>
                </div>`
            },"""
frost_new = """            {
                l: '13. ASTRAL PROJECTION', cls: 'glass',
                f: `<div class="f-astral c-f c">
                    <div class="astral-ring"></div>
                    <div class="astral-txt">Jay Lin</div>
                </div>`,
                b: `<div class="b-astral c-b c">
                    <div style="font-family:var(--font-serif); font-size:24px; font-style:italic;">${p.n}</div>
                    <div class="astral-box">${p.r}</div>
                    <div class="astral-box">${p.e}</div>
                    <div class="astral-box">${p.w}</div>
                </div>`
            },"""
content = content.replace(frost_old, frost_new)

botanic_old = """                        <svg class="bot-art" viewBox="0 0 200 300" preserveAspectRatio="xMidYMid slice">
                            <path d="M 90 20 C 130 20 150 50 150 90 C 150 110 140 130 130 150 C 120 160 130 180 140 210 C 160 250 180 280 200 300 L 40 300 C 30 250 20 220 30 170 C 40 130 60 110 60 70 C 60 40 70 20 90 20 Z" fill="#181a1c" />
                            <path d="M 130 110 C 110 115 90 110 80 120 C 70 130 65 150 70 170" stroke="#e2e8f0" fill="none" stroke-width="0.5"/>
                            <path d="M 150 90 Q 120 80 100 100" stroke="#e2e8f0" fill="none" stroke-width="0.5"/>
                            <path d="M110 80 Q125 70 135 85 Q145 95 150 90 Q140 98 125 102 Q110 95 100 105 Q105 100 110 80 Z" fill="#d8cfe6"/>
                            <path d="M140 50 L141 54 L145 55 L141 56 L140 60 L139 56 L135 55 L139 54 Z" fill="#a9b5c2" opacity="0.8"/>
                            <path d="M60 120 L62 128 L70 130 L62 132 L60 140 L58 132 L50 130 L58 128 Z" fill="#a9b5c2" opacity="0.4" transform="scale(0.6) translate(40, -40)"/>
                            <g class="bot-flower" transform="translate(80, 180)">
                                <path d="M0 0 C 10 -20 30 -20 40 0 C 50 20 30 40 20 40 C 0 40 -10 20 0 0" fill="#90bcf0"/>
                                <circle cx="20" cy="15" r="5" fill="#181a1c"/>
                                <path d="M20 15 L25 5 M20 15 L10 5 M20 15 L30 25 M20 15 L5 25" stroke="#181a1c" stroke-width="0.5"/>
                            </g>
                            <g class="bot-flower" transform="translate(120, 220) scale(0.8)">
                                <path d="M0 0 C 10 -20 30 -20 40 0 C 50 20 30 40 20 40 C 0 40 -10 20 0 0" fill="#90bcf0"/>
                                <circle cx="20" cy="15" r="5" fill="#181a1c"/>
                                <path d="M20 15 L25 5 M20 15 L10 5 M20 15 L30 25 M20 15 L5 25" stroke="#181a1c" stroke-width="0.5"/>
                            </g>
                            <g class="bot-flower" transform="translate(50, 240) scale(0.9) rotate(-20)">
                                <path d="M0 0 C 10 -20 30 -20 40 0 C 50 20 30 40 20 40 C 0 40 -10 20 0 0" fill="#90bcf0"/>
                                <circle cx="20" cy="15" r="5" fill="#181a1c"/>
                                <path d="M20 15 L25 5 M20 15 L10 5 M20 15 L30 25 M20 15 L5 25" stroke="#181a1c" stroke-width="0.5"/>
                            </g>
                            <path d="M100 195 Q90 220 120 235 M120 235 Q130 260 70 255" fill="none" stroke="#90bcf0" stroke-width="1.5"/>
                        </svg>"""
botanic_new = """                        <svg class="bot-art" viewBox="0 0 200 300" preserveAspectRatio="xMidYMid slice">
                            <path d="M 90 20 C 130 20, 150 40, 150 70 C 150 80, 140 85, 135 90 L 155 105 L 140 115 L 145 120 L 135 125 L 145 140 C 120 155, 120 170, 125 190 C 150 220, 180 260, 190 300 L 20 300 C 10 250, 20 200, 50 170 C 60 140, 50 100, 55 60 C 60 30, 70 20, 90 20 Z" fill="#181a1c" />
                            <path d="M 135 90 L 155 105 L 140 115 L 145 120 L 135 125 L 145 140" fill="none" stroke="#38bdf8" stroke-width="1.5" />
                            <path d="M 115 85 Q 120 85, 120 90 Q 115 95, 110 90" fill="none" stroke="#e2e8f0" stroke-width="1" />
                            <path d="M 90 20 C 130 20, 150 40, 150 70" fill="none" stroke="#38bdf8" stroke-width="1" />
                            <circle cx="115" cy="90" r="2" fill="#38bdf8"/>
                            <path d="M 100 160 L 120 165 L 115 180 L 95 175 Z" fill="#1f2937" stroke="#38bdf8" stroke-width="0.5"/>
                            <path d="M 70 120 L 90 120 L 90 140 L 70 140 Z" fill="none" stroke="#e2e8f0" stroke-width="0.5"/>
                            <path d="M 80 125 L 85 125 L 85 135 L 80 135 Z" fill="#38bdf8"/>
                        </svg>"""
content = content.replace(botanic_old, botanic_new)

contour_old = """                        <circle cx="60" cy="110" r="10" fill="#facc15" />
                        <circle cx="150" cy="150" r="18" fill="#facc15" />
                        <circle cx="170" cy="135" r="5" fill="#facc15" />
                        
                        <g filter="url(#engrave)">
                            <path class="contour-line" d="M80 80 C60 100 40 120 70 150 C90 170 100 200 80 230 C60 260 50 300 50 300" />
                            <path class="contour-line" d="M90 70 C130 90 160 120 180 180 C200 220 220 260 220 300" />
                            <path class="contour-line outline-blue" d="M50 180 C90 180 110 200 130 250" />
                            <path class="contour-line outline-blue" d="M120 160 C150 160 180 140 200 110" />
                            <path class="contour-line" d="M85 130 C95 120 105 125 115 128" />
                            <circle cx="100" cy="132" r="2.5" fill="#1f2a33"/>
                            
                            <circle cx="60" cy="185" r="3" fill="#1f2a33" class="contour-black-dot"/>
                            <circle cx="140" cy="100" r="4" fill="#1f2a33" class="contour-black-dot"/>
                        </g>"""
contour_new = """                        <path d="M 50 120 Q 100 90, 150 120 Q 140 135, 100 135 Q 60 135, 50 120 Z" fill="#facc15" opacity="0.8"/>
                        <circle cx="100" cy="122" r="6" fill="#1f2a33" />
                        <circle cx="102" cy="120" r="2" fill="#fff" />
                        
                        <g filter="url(#engrave)">
                            <path class="contour-line" d="M 40 120 Q 100 80, 160 120" />
                            <path class="contour-line" d="M 45 110 Q 100 70, 155 110" />
                            <path class="contour-line" d="M 50 120 Q 100 145, 150 120" />
                            <path class="contour-line" d="M 30 80 Q 90 50, 160 70" />
                            <path class="contour-line outline-blue" d="M 80 160 L 120 160 L 110 180 L 90 180 Z" />
                            <path class="contour-line" d="M 100 180 L 100 230" />
                            <path class="contour-line outline-blue" d="M 70 200 L 130 200" />
                            <circle cx="100" cy="230" r="4" fill="#1f2a33" class="contour-black-dot"/>
                        </g>"""
content = content.replace(contour_old, contour_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

# ================================ CSS REPLACEMENTS ================================
css_path = r'e:\2026 spring\business cards\css\cards.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Card 06
mesh_css_old = """/* =========================================================================
   DESIGN 06: FLUID MESH
   Abstract mesh gradients, frosted glass typography
   ========================================================================= */
.f-mesh {
    background: radial-gradient(circle at top left, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 40px;
}

.f-mesh::before {
    content: '';
    position: absolute;
    width: 200%;
    height: 200%;
    top: -50%;
    left: -50%;
    background: radial-gradient(circle at center, #a18cd1 0%, transparent 50%), radial-gradient(circle at bottom right, #fbc2eb 0%, transparent 50%);
    filter: blur(60px);
    z-index: 0;
}

.mesh-glass {
    position: relative;
    z-index: 1;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    padding: 20px;
    border-radius: 20px;
    color: #fff;
}

.mesh-name {
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 5px;
}

.mesh-title {
    font-size: 14px;
    font-weight: 500;
    opacity: 0.9;
}

.b-mesh {
    background: #fff;
    color: #333;
    padding: 40px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.mesh-row {
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 15px;
    border-bottom: 1px solid #eee;
    padding-bottom: 15px;
}

.mesh-row:last-child {
    border-bottom: none;
}"""
mesh_css_new = """/* =========================================================================
   DESIGN 06: MECHA BLUEPRINT
   Minimal sci-fi schematic blueprint
   ========================================================================= */
.f-mecha {
    background: #001a33;
    background-image: 
        linear-gradient(rgba(0, 150, 255, 0.2) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 150, 255, 0.2) 1px, transparent 1px);
    background-size: 20px 20px;
    color: #00aaff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid rgba(0, 150, 255, 0.5);
    box-shadow: inset 0 0 30px rgba(0, 100, 255, 0.5);
}
.mecha-hud {
    border: 1px solid #00aaff;
    padding: 20px;
    background: rgba(0, 50, 100, 0.5);
    text-transform: uppercase;
    font-family: var(--font-mono);
    text-align: center;
    position: relative;
}
.mecha-hud::before {
    content: '';
    position: absolute;
    top: -5px; left: -5px; width: 10px; height: 10px;
    border-top: 2px solid #00aaff; border-left: 2px solid #00aaff;
}
.mecha-hud::after {
    content: '';
    position: absolute;
    bottom: -5px; right: -5px; width: 10px; height: 10px;
    border-bottom: 2px solid #00aaff; border-right: 2px solid #00aaff;
}
.mecha-name {
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 5px;
}
.mecha-title {
    font-size: 9px;
    letter-spacing: 2px;
    opacity: 0.8;
}
.b-mecha {
    background: #001a33;
    color: #00aaff;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-family: var(--font-mono);
    border: 1px solid rgba(0, 150, 255, 0.5);
}
.mecha-row {
    font-size: 11px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px dashed rgba(0, 150, 255, 0.3);
    padding-bottom: 15px;
}
.mecha-row span {
    font-weight: 800;
    opacity: 0.5;
}"""
css = css.replace(mesh_css_old, mesh_css_new)


# Replace Card 11
typo_css_old = """/* =========================================================================
   DESIGN 11: MINIMAL TYPOGRAPHY
   Black and white minimal grid structure
   ========================================================================= */
.f-min-typo {
    background: #ffffff;
    color: #000;
}

.mt-wrap {
    width: 100%;
    height: 100%;
    position: relative;
    padding: 40px;
}

.mt-title {
    font-size: 64px;
    line-height: 1;
    font-weight: 900;
    letter-spacing: -2px;
    margin-bottom: -10px;
}

.mt-subtitle {
    font-size: 64px;
    line-height: 1;
    font-weight: 900;
    letter-spacing: -2px;
    padding-left: 60px;
}

.mt-en-title {
    margin-top: 30px;
    font-size: 12px;
    font-family: var(--font-mono);
    font-weight: 600;
    letter-spacing: 2px;
}

.mt-line-vert {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 40px;
    width: 2px;
    background: #000;
}

.mt-line-horiz {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 80px;
    height: 2px;
    background: #000;
}

.b-min-typo {
    background: #ffffff;
    color: #000;
    display: flex;
    padding: 40px;
}

.mt-b-wrap {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.mt-b-left {
    border-bottom: 2px solid #000;
    padding-bottom: 20px;
}

.mt-b-name {
    font-size: 32px;
    font-weight: 900;
}

.mt-b-role {
    font-size: 12px;
    font-family: var(--font-mono);
}

.mt-b-right {
    display: flex;
    flex-direction: column;
    gap: 15px;
    font-size: 12px;
    font-weight: 600;
}

.mt-b-row {
    display: flex;
    align-items: center;
    gap: 15px;
}"""
typo_css_new = """/* =========================================================================
   DESIGN 11: NEO-TOKYO TYPOGRAPHY
   Futuristic brutalist layout
   ========================================================================= */
.f-neo-typo {
    background: #e6e6e6;
    color: #111;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}
.nt-wrap {
    text-align: center;
    z-index: 1;
}
.nt-title {
    font-family: var(--font-display);
    font-size: 60px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 0.9;
}
.nt-subtitle {
    font-family: var(--font-display);
    font-size: 60px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 0.9;
}
.nt-en-title {
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 15px;
    color: #e32636;
}
.b-neo-typo {
    background: #111;
    color: #eee;
    padding: 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.nt-b-name {
    font-size: 24px;
    font-weight: 900;
    text-transform: uppercase;
}
.nt-b-role {
    font-size: 11px;
    color: #e32636;
    letter-spacing: 3px;
    margin-bottom: 30px;
}
.nt-b-row {
    font-family: var(--font-mono);
    font-size: 11px;
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}"""
css = css.replace(typo_css_old, typo_css_new)


obs_css_old = """/* =========================================================================
   DESIGN 12: OBSIDIAN GLASS
   Deep dark luxurious glass with aura reflection gradient
   ========================================================================= */
.f-obs {
    background: #050505;
    color: #efefef;
    display: flex;
    align-items: flex-end;
    padding: 40px;
    position: relative;
    overflow: hidden;
}

.f-obs::before {
    content: '';
    position: absolute;
    top: -50%;
    left: 0%;
    width: 150%;
    height: 150%;
    background: conic-gradient(from 180deg at 50% 50%, #2a8af6 0deg, #a853ba 180deg, #e92a67 360deg);
    filter: blur(80px);
    opacity: 0.2;
    z-index: 0;
}

.obs-glass {
    position: relative;
    z-index: 1;
    width: 100%;
    padding: 30px;
    background: rgba(20, 20, 20, 0.4);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
}

.obs-title {
    font-size: 36px;
    font-weight: 200;
    letter-spacing: 4px;
}

.b-obs {
    background: #050505;
    color: #efefef;
    padding: 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.obs-logo {
    font-size: 120px;
    font-weight: 900;
    -webkit-text-stroke: 1px rgba(255, 255, 255, 0.1);
    color: transparent;
    letter-spacing: -10px;
}

.obs-list {
    display: flex;
    flex-direction: column;
    gap: 15px;
    width: 60%;
    z-index: 1;
}

.obs-item {
    background: rgba(255, 255, 255, 0.03);
    padding: 15px 20px;
    border-radius: 8px;
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 15px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}"""
obs_css_new = """/* =========================================================================
   DESIGN 12: DARK MATTER NEXUS
   Dark space core with glowing purple aura
   ========================================================================= */
.f-dark-nexus {
    background: radial-gradient(circle at center, #1a1a2e 0%, #000 80%);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
}
.nexus-core {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: #000;
    box-shadow: 0 0 50px #4f46e5, inset 0 0 20px #818cf8;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgba(129, 140, 248, 0.5);
}
.nexus-title {
    font-family: var(--font-display);
    font-size: 30px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #818cf8;
    text-shadow: 0 0 10px #4f46e5;
}
.b-dark-nexus {
    background: #000;
    color: #818cf8;
    padding: 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 20px;
    border: 1px solid rgba(79, 70, 229, 0.3);
}
.nexus-item {
    font-family: var(--font-mono);
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
    opacity: 0.8;
}"""
css = css.replace(obs_css_old, obs_css_new)


frost_css_old = """/* =========================================================================
   DESIGN 13: FROSTED POLYCARBONATE
   Clean, white glassmorphism
   ========================================================================= */
.f-frost {
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(40px);
    border: 1px solid rgba(255, 255, 255, 0.8);
    color: #111;
    display: flex;
    align-items: flex-end;
    padding: 40px;
    box-shadow: inset 0 0 50px rgba(255, 255, 255, 0.5);
}

.frost-txt {
    font-size: 48px;
    font-weight: 300;
    letter-spacing: -2px;
}

.b-frost {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(40px);
    border: 1px solid rgba(255, 255, 255, 0.8);
    padding: 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 20px;
}

.frost-box {
    background: rgba(255, 255, 255, 0.9);
    padding: 15px 20px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    color: #333;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}"""
frost_css_new = """/* =========================================================================
   DESIGN 13: ASTRAL PROJECTION
   Rotating magic circle projection
   ========================================================================= */
.f-astral {
    background: rgba(20, 20, 40, 0.6);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #e0e7ff;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}
.astral-ring {
    position: absolute;
    width: 250px;
    height: 250px;
    border-radius: 50%;
    border: 1px dashed rgba(167, 139, 250, 0.5);
    animation: rotate 20s linear infinite;
}
.astral-txt {
    font-family: var(--font-serif);
    font-size: 32px;
    font-style: italic;
    font-weight: 400;
    text-shadow: 0 0 20px rgba(167, 139, 250, 0.8);
    z-index: 1;
}
.b-astral {
    background: linear-gradient(135deg, #1e1b4b, #312e81);
    color: #ddd;
    padding: 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 15px;
}
.astral-box {
    background: rgba(255, 255, 255, 0.05);
    padding: 15px;
    border-radius: 8px;
    font-family: var(--font-ui);
    font-size: 11px;
    letter-spacing: 1px;
    border-left: 2px solid #a78bfa;
}
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}"""
css = css.replace(frost_css_old, frost_css_new)


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Files successfully updated!")
