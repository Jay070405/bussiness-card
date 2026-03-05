import sys

html_path = r'e:\2026 spring\business cards\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

metropolo_old = """            {
                l: '02. METROPOLO (EXECUTIVE GOLD)', cls: 'matte',
                f: `<div class="f-metro c-f c">
                    <div class="metro-signature">Jay Lin</div>
                    <div class="metro-brand">CONCEPT DESIGNER</div>
                    <div class="gloss" style="mix-blend-mode:color-dodge; opacity:0.1;"></div>
                </div>`,
                b: `<div class="b-metro c-b c">
                    <div class="metro-name-ch">林 杰</div>
                    <div class="metro-title-ch">概念设计师</div>
                    <div class="metro-name-en">${p.n}</div>
                    <div class="metro-title-en">${p.r}</div>
                    
                    <div class="metro-contact">
                        <span>Phone:</span> ${p.v}<br>
                        <span>Email:</span> ${p.e}<br>
                        <span>Web:</span> ${p.w}
                    </div>
                    
                    <div class="metro-qr">
                        <div></div><div></div><div></div>
                        <div></div><div style="background:transparent;"></div><div></div>
                        <div></div><div></div><div></div>
                    </div>
                </div>`
            },"""

metropolo_new = """            {
                l: '02. HOLOGRAPHIC CUTOUT', cls: 'holo',
                f: `<div class="f-holo c-f c">
                    <div class="holo-base">
                        <div class="holo-cutout">
                            <div class="holo-inner"></div>
                        </div>
                        <div class="holo-logotype">
                            <div class="holo-logo-text">J. LIN DESIGN</div>
                            <div class="holo-logo-sub">CONCEPTUAL ART & WORLD BUILDING</div>
                        </div>
                    </div>
                </div>`,
                b: `<div class="b-holo c-b c">
                    <div class="holo-b-wrap">
                        <div class="holo-cutout small">
                            <div class="holo-inner"></div>
                        </div>
                        <div class="holo-contact">
                            <div style="font-size:16px; font-weight:700; color:#fff;">${p.n}</div>
                            <div style="font-size:9px; color:#aaa; letter-spacing:2px; margin-bottom:20px;">${p.r}</div>
                            <div class="holo-row"><span>MAIL</span>${p.e}</div>
                            <div class="holo-row"><span>SITE</span>${p.w}</div>
                        </div>
                    </div>
                </div>`
            },"""
content = content.replace(metropolo_old, metropolo_new)

xiuyilou_old = """            {
                l: '03. XIUYILOU (HERITAGE FOIL)', cls: 'holo',
                f: `<div class="f-xiu c-f c">
                    <div class="xiu-butterfly"></div>
                    <div class="xiu-brand">J A Y   L I N</div>
                    <div class="xiu-sub">概 | 念 | 设 | 计</div>
                    <div class="gloss" style="opacity:0.2;"></div>
                </div>`,
                b: `<div class="b-xiu c-b c">
                    <div class="xiu-top-lbl">
                        <span>概 | 念 | 设 | 计</span>
                        <span>艺 | 术</span>
                    </div>
                    
                    <div class="xiu-name-line">
                        林 杰 <span>| JAY LIN</span>
                    </div>
                    
                    <div class="xiu-rank-bar">
                        <span style="font-family:var(--font-cjk); font-size:10px;">承接：角色 / 场景 / 概念</span>
                        <div class="xiu-blocks">
                            <div class="xiu-block"></div><div class="xiu-block"></div>
                        </div>
                        <span style="color:#3a2b12;">/</span>
                        <div class="xiu-blocks">
                            <div class="xiu-block"></div><div class="xiu-block"></div><div class="xiu-block dim"></div>
                        </div>
                    </div>
                    
                    <div class="xiu-footer">
                        Email: ${p.e}<br>
                        Web: ${p.w}
                    </div>
                    
                    <div class="xiu-calligraphy-bg">
                        概<br>念<br>艺<br>术
                    </div>
                </div>`
            },"""
xiuyilou_new = """            {
                l: '03. BOTANICAL SILHOUETTE', cls: 'matte',
                f: `<div class="f-botanic c-f c">
                    <div class="bot-frame">
                        <div class="bot-title-vert">J. LIN</div>
                        <div class="bot-title-horiz">CONCEPT DESIGN</div>
                        <svg class="bot-art" viewBox="0 0 200 300" preserveAspectRatio="xMidYMid slice">
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
                        </svg>
                    </div>
                </div>`,
                b: `<div class="b-botanic c-b c">
                    <div class="bot-b-wrap">
                        <div class="bot-b-title">${p.n}</div>
                        <div class="bot-b-sub">${p.r}</div>
                        <div class="bot-b-contact">
                            <div>${p.e}</div>
                            <div>${p.w}</div>
                        </div>
                    </div>
                </div>`
            },"""
content = content.replace(xiuyilou_old, xiuyilou_new)

swiss_old = """            {
                l: '11. SWISS POSTER', cls: 'matte',
                f: `<div class="f-swiss c-f c">
                    <div class="swiss-header">JAY LIN</div>
                    <div class="swiss-footer">DESIGN<br>SYSTEM</div>
                </div>`,
                b: `<div class="b-swiss c-b c">
                    <div class="swiss-block">${icoW} ${p.v}</div>
                    <div class="swiss-block">${icoG} ${p.w}</div>
                    <div class="swiss-block">${icoL} ${p.l}</div>
                </div>`
            },"""
swiss_new = """            {
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
content = content.replace(swiss_old, swiss_new)

void_old = """            {
                l: '15. VANTABLACK (VOID)', cls: 'matte',
                f: `<div class="f-void c-f c">
                    <div class="void-txt">JAY LIN</div>
                </div>`,
                b: `<div class="b-void c-b c">
                    <div class="void-reveal">${p.r}<br><br>${p.e}<br>${p.w}</div>
                </div>`
            }
        ];"""
void_new = """            {
                l: '15. VANTABLACK (VOID)', cls: 'matte',
                f: `<div class="f-void c-f c">
                    <div class="void-txt">JAY LIN</div>
                </div>`,
                b: `<div class="b-void c-b c">
                    <div class="void-reveal">${p.r}<br><br>${p.e}<br>${p.w}</div>
                </div>`
            },
            {
                l: '16. ETHEREAL FLUID', cls: 'matte',
                f: `<div class="f-fluid c-f c">
                    <div class="fluid-bg"></div>
                    <div class="fluid-glass">
                        <div class="fluid-icon"></div>
                        <div class="fluid-title">JAY LIN<br><span>CONCEPT DESIGN</span></div>
                    </div>
                </div>`,
                b: `<div class="b-fluid c-b c">
                    <div class="fluid-contact">
                        <div style="font-size:16px; font-weight:700; color:#fff;">${p.n}</div>
                        <div style="font-size:10px; color:#aaa; margin-bottom:15px;">${p.r}</div>
                        <div class="fluid-row">${p.e}</div>
                        <div class="fluid-row">${p.w}</div>
                    </div>
                </div>`
            },
            {
                l: '17. EMBOSSED ANIME CONTOUR', cls: 'matte',
                f: `<div class="f-contour c-f c">
                    <div class="contour-bg"></div>
                    <svg class="contour-svg" viewBox="0 0 200 300">
                        <defs>
                            <filter id="engrave" x="-20%" y="-20%" width="140%" height="140%">
                                <feDropShadow dx="-2" dy="-2" stdDeviation="2" flood-color="#ffffff" flood-opacity="1"/>
                                <feDropShadow dx="2" dy="2" stdDeviation="2" flood-color="#94a3b8" flood-opacity="0.5"/>
                            </filter>
                        </defs>
                        <circle cx="60" cy="110" r="10" fill="#facc15" />
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
                        </g>
                    </svg>
                    <div class="contour-title">JAY LIN</div>
                </div>`,
                b: `<div class="b-contour c-b c">
                    <div class="contour-info">
                        <div style="font-size:20px; font-weight:800; color:#1f2a33;">${p.n}</div>
                        <div style="font-size:12px; font-weight:600; color:#38bdf8; margin-bottom:20px; letter-spacing:2px;">${p.r}</div>
                        <div class="contour-row">${p.e}</div>
                        <div class="contour-row">${p.w}</div>
                    </div>
                </div>`
            },
            {
                l: '18. FROSTED GRIMOIRE', cls: 'glass',
                f: `<div class="f-grim c-f c">
                    <div class="grim-bg"></div>
                    <div class="grim-circle">
                        <div class="grim-runes">&#x274B;</div>
                    </div>
                    <div class="grim-overlay"></div>
                    <div class="grim-title">GRIMOIRE</div>
                </div>`,
                b: `<div class="b-grim c-b c">
                    <div class="grim-text">
                        <div style="color:#d4af37; font-size:16px; margin-bottom:10px;">${p.n}</div>
                        <div style="color:#fff; font-size:10px;">${p.r}</div>
                        <br>
                        <div style="color:#aaa; font-size:10px;">${p.e}<br>${p.w}</div>
                    </div>
                </div>`
            },
            {
                l: '19. PRISMATIC CRYSTAL', cls: 'glass',
                f: `<div class="f-prism c-f c">
                    <div class="prism-shard"></div>
                    <div class="prism-title">J.L</div>
                </div>`,
                b: `<div class="b-prism c-b c">
                    <div class="prism-content">
                        <div style="font-size:16px; color:#555;">${p.n}</div>
                        <div style="font-size:10px; color:#999; margin-bottom:20px;">${p.r}</div>
                        <div style="font-size:10px; color:#777;">${p.e}<br>${p.w}</div>
                    </div>
                </div>`
            },
            {
                l: '20. FLOATING SIGIL', cls: 'matte',
                f: `<div class="f-sigil c-f c">
                    <div class="sigil-mark">&#x27E1;</div>
                    <div class="sigil-title">CONCEPTUAL</div>
                </div>`,
                b: `<div class="b-sigil c-b c">
                    <div class="sigil-info">
                        <div style="color:#e2e8f0; font-size:16px;">${p.n}</div>
                        <div style="color:#94a3b8; font-size:10px; margin-bottom:20px;">${p.r}</div>
                        <div style="color:#64748b; font-size:10px;">${p.e}<br>${p.w}</div>
                    </div>
                </div>`
            }
        ];"""
content = content.replace(void_old, void_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML Replaced successfully")
