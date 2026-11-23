"""Builds the 5 KALAGNI pages from shared parts + content taken from the company profile PDF.
Tokens: ~R~ = path to site root ("" or "../"), ~P~ = path to pages folder ("pages/" or "")."""
import pathlib, html, sys

# Project root = the folder above this script (works on any computer).
# Optional: pass another folder to write the pages somewhere else, e.g. for comparing.
ROOT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
PHONE_DISPLAY, PHONE_TEL = "+91 9912485530", "+919912485530"
EMAIL = "info@kalagni.co.in"
WHATSAPP = "https://wa.me/919912485530"

def esc(s):
    return html.escape(s, quote=True)

# =====================================================================
# DATA (from "KALAGNI profile 01.pdf"; typos in the slides corrected)
# =====================================================================
SERVICES = [
  dict(id="electrical", group="power", icon="bi-lightning-charge", img="service-electrical.jpg",
    name="Electrical Power Infrastructure", title='Electrical Power <span>Infrastructure</span>',
    short="HT/LT networks, GIS &amp; AIS substations, underground cables, transmission lines and control panels.",
    mega="Substations, HT/LT systems, cable networks",
    tagline="Engineering · Execution · Testing · Commissioning",
    quote="Powering infrastructure for a brighter tomorrow.",
    intro=["KALAGNI Integrated Projects Private Limited provides electrical power infrastructure engineering and project delivery services across HT/LT networks, substations, cable infrastructure, electrical distribution and transmission systems.",
           "Our EPC delivery model connects concept design, engineering, statutory approval coordination, procurement, installation, testing, commissioning, handover and lifecycle support, according to the contracted scope."],
    cap_title='Our Core <span>Capabilities</span>', cap_sub="Reliable power infrastructure for industries, cities and communities",
    caps=[
      ("bi-rulers", "Concept Design &amp; Custom Engineering", ["Load-flow studies and short-circuit analysis", "Single-line diagrams and design documentation", "Protection and relay coordination", "Substation layouts and equipment planning", "Earthing and lightning-protection design", "Project-specific panel, cable and network design"]),
      ("bi-plug", "HT &amp; LT Electrical Systems", ["HT/LT electrical infrastructure", "Transformers, switchgear and ring main units (RMUs)", "HT/LT panels and distribution systems", "Bus ducts and associated electrical infrastructure", "Power distribution for industrial and commercial facilities"]),
      ("bi-diagram-3", "Substations: GIS &amp; AIS", ["Engineering and coordination for gas-insulated and air-insulated substations", "Transformer, switchgear, protection and control interfaces", "Auxiliary systems and SCADA integration where specified", "Installation, testing and commissioning"]),
      ("bi-bezier2", "Underground Cable Networks", ["HT/LT cable routing and network planning", "Trench and duct coordination", "Cable laying, jointing and termination", "Inspection and testing according to project specifications"]),
      ("bi-broadcast", "Overhead Transmission Lines", ["Transmission-line engineering and project coordination", "Tower and conductor-related design coordination", "Foundation, erection and stringing activities", "Line testing and commissioning support"]),
      ("bi-toggles", "Electrical Panels &amp; Control Systems", ["PCC and MCC panels", "APFC panels", "PLC and SCADA panels and interfaces", "Energy metering and automation", "BMS integration where specified"]),
    ],
    approach=[("bi-shield-check", "Compliance First", "Plan work around applicable statutory requirements, approved specifications and relevant technical standards."),
              ("bi-lightbulb", "Design-Led Solutions", "Develop project-specific engineering solutions based on requirements, site conditions and coordinated design."),
              ("bi-people", "Single-Point EPC Responsibility", "Provide a coordinated point of responsibility for the work packages included in the contract."),
              ("bi-arrow-repeat", "Lifecycle Support", "Support preventive maintenance, breakdown response and asset documentation where contracted.")],
    panel=dict(icon="bi-file-earmark-check", title='Statutory Approvals <span>Coordination</span>',
               text="Depending on project requirements, location and applicable regulations, KALAGNI can coordinate documentation and interfaces with relevant authorities and utilities, such as:",
               items=["CEIG or the applicable Electrical Inspectorate", "DISCOMs and transmission utilities", "PESO, where applicable to the project", "Other relevant statutory bodies and approval authorities"],
               note="Approvals remain subject to the competent authority's requirements and decisions. The exact authority names, jurisdiction and applicability are confirmed for each project."),
    value_text="KALAGNI aims to provide customised, reliable and future-ready power infrastructure through engineering-led planning, coordinated execution and responsible project delivery.",
  ),
  dict(id="solar-bess", group="power", icon="bi-sun", img="service-solar-bess.jpg",
    name="Solar & BESS Solutions", title='Solar &amp; <span>BESS Solutions</span>',
    short="Rooftop and ground-mounted solar, battery energy storage, grid connection and PPA support.",
    mega="Solar PV, battery storage, grid connection",
    tagline="Clean Energy · Reliable Power · Sustainable Growth",
    quote="Powering a cleaner, brighter tomorrow.",
    intro=["KALAGNI Integrated Projects Private Limited delivers end-to-end solar and battery energy storage system (BESS) solutions through engineering, project coordination and execution support, enabling cleaner energy, reliable power and sustainable growth for industrial, commercial and infrastructure projects.",
           "Our integrated approach combines solar power generation and energy storage solutions to support grid connectivity, energy reliability and future-ready power infrastructure, according to project requirements."],
    cap_title='Our <span>Capabilities</span>', cap_sub="Integrated solar &amp; BESS project delivery",
    caps=[
      ("bi-sun", "Solar PV Systems", ["Rooftop and ground-mounted solutions", "Engineering and design (as per project scope)", "Performance analysis and energy yield estimation", "Balance of system integration"]),
      ("bi-battery-charging", "Battery Energy Storage Systems (BESS)", ["BESS system engineering and design", "Integration with solar and grid systems", "Energy management and control systems", "Peak shaving, backup and reliability solutions (as per project scope)"]),
      ("bi-gear-wide-connected", "Electrical Integration", ["Inverters, transformers and switchgear integration", "HT/LT evacuation support", "Protection, metering and control systems", "SCADA / remote monitoring (as per scope)", "Grid code compliance"]),
      ("bi-broadcast", "Grid Connection &amp; PPA Support", ["Technical studies and documentation support", "Grid connectivity coordination with DISCOMs", "PPA process support (where applicable)", "Metering and interconnection requirements", "Compliance with applicable grid codes and regulations"]),
      ("bi-cone-striped", "Project Execution", ["Detailed engineering and procurement support", "Installation and civil works coordination", "Testing and commissioning", "Performance monitoring", "Handover and documentation"]),
      ("bi-tools", "Operation &amp; Maintenance", ["Preventive maintenance support", "Performance monitoring and reporting", "Troubleshooting support", "Spare management support", "Lifecycle support (as per contract)"]),
    ],
    panels2=[
      dict(icon="bi-file-earmark-check", title='Regulatory Support &amp; <span>Compliance</span>',
           text="We coordinate with relevant authorities and follow applicable regulations, standards and grid requirements, including:",
           items=["DISCOMs &amp; utilities", "Grid codes &amp; connectivity requirements", "PPA support (where applicable)", "Government policies &amp; incentives", "Applicable standards and norms"]),
      dict(icon="bi-journal-check", title='Applicable Standards &amp; <span>Guidelines</span>',
           text="As per project requirements:",
           items=["CEA Regulations", "MNRE Guidelines", "DISCOM Technical Requirements", "Grid Code Compliance", "IEEE / IEC Standards", "IS Standards", "Safety and Earthing Norms", "Environmental and Regulatory Requirements"], two_col=True),
    ],
    values=[("bi-tree", "Cleaner Energy", "Support renewable energy adoption and lower carbon footprint."),
            ("bi-graph-up-arrow", "Reliable Power", "Enhance energy reliability and operational continuity."),
            ("bi-currency-rupee", "Optimised Cost", "Design efficient and sustainable solutions based on project needs."),
            ("bi-buildings", "Future-Ready Infrastructure", "Enable scalable solutions for long-term growth.")],
    sectors=[("bi-sun", "Solar PV Solutions"), ("bi-battery-charging", "BESS Solutions"), ("bi-broadcast", "Grid Connectivity"), ("bi-gear", "Engineering &amp; Execution"), ("bi-bar-chart-line", "Sustainable Growth")],
  ),
  dict(id="infrastructure", group="build", icon="bi-buildings", img="service-infrastructure.jpg",
    name="Infrastructure & Construction", title='Infrastructure &amp; <span>Construction</span>',
    short="Industrial, commercial and residential buildings, civil works and land development.",
    mega="Industrial, commercial &amp; residential",
    tagline="Plan · Design · Build · Deliver",
    quote="Building infrastructure for a stronger tomorrow.",
    intro=["KALAGNI Integrated Projects Private Limited delivers high-quality infrastructure and construction solutions for industrial, commercial, residential and allied developments through a planned, engineering-led and execution-focused approach.",
           "We combine architectural and engineering design, civil construction, MEP integration and project management to deliver functional, safe, sustainable and future-ready built environments."],
    cap_title='Our <span>Capabilities</span>', cap_sub="Integrated civil &amp; infrastructure solutions",
    caps=[
      ("bi-building-gear", "Industrial Buildings", ["Factory and plant buildings", "Pre-engineered and RCC structures", "Production and utility buildings", "Structural and architectural works", "Civil and MEP integration", "Project execution and handover"]),
      ("bi-building", "Commercial Projects", ["Office buildings", "Commercial complexes", "Retail and mixed-use developments", "Structural, architectural and MEP works", "Interior and external civil works", "End-to-end project delivery"]),
      ("bi-house-door", "Residential Projects", ["Residential apartments", "Villas and gated communities", "Structural and architectural construction", "MEPF integration", "External development and landscaping", "Quality construction and timely delivery"]),
      ("bi-signpost-split", "Civil Works &amp; Land Development", ["Site development and grading", "Internal and external roads", "Drainage and storm-water systems", "Boundary walls and compound works", "Earthwork and retaining structures", "Utilities and external infrastructure", "Master planning support"]),
      ("bi-check2-square", "Integration &amp; Handover", ["Coordination with MEPF systems", "Finishing and external works", "Testing, documentation and handover", "Compliance with applicable standards and approvals", "Support for O&amp;M where contracted"]),
    ],
    approach=[("bi-cone-striped", "Planned Execution", "Structured planning, coordinated design and efficient execution."),
              ("bi-patch-check", "Quality &amp; Safety First", "Adherence to quality standards, safety practices and site management systems."),
              ("bi-diagram-3", "Integrated Delivery", "Coordination across civil, structural, architectural and MEPF packages."),
              ("bi-tree", "Sustainable &amp; Future-Ready", "Focus on durable, efficient and environmentally responsible construction.")],
    panel=dict(icon="bi-award", title='Construction Experience &amp; <span>Leadership Strength</span>',
               confirm="CONFIRM before publishing: the profile spells this name 'Dr. Vinod Durgam' here but 'Vinod Duram' on the leadership slide, and the company 'BrickCem Construction Private Limited' here but 'Busikem Indian Construction' on the leadership slide.",
               text="Dr. Vinod Durgam brings over 15 years of business ownership experience through BrickCem Construction Private Limited, with proven experience in construction, infrastructure development and business operations. This experience adds strong industry understanding and execution insight to KALAGNI's infrastructure and construction capabilities.",
               items=["15+ years of construction experience", "Infrastructure development", "Business operations"]),
    values=[("bi-buildings", "Functional Spaces", "Design and build spaces that support your operations and growth."),
            ("bi-clock-history", "Timely Delivery", "Planned execution with milestone-based tracking."),
            ("bi-shield-check", "Reliable Quality", "Focus on quality construction and long-term durability."),
            ("bi-tree", "Sustainable Development", "Infrastructure that supports people, business and the environment.")],
  ),
  dict(id="mepf", group="build", icon="bi-gear-wide-connected", img="service-mepf.jpg",
    name="MEPF Engineering", title='MEPF <span>Engineering</span>',
    short="Integrated mechanical, electrical, plumbing and fire protection design and execution.",
    mega="Mechanical, electrical, plumbing &amp; fire",
    tagline="Integrated Systems · Efficient Buildings · Better Spaces",
    quote="Integrated engineering for comfort, safety and performance.",
    intro=["KALAGNI Integrated Projects Private Limited delivers integrated MEPF (Mechanical, Electrical, Plumbing and Fire Protection) solutions for industrial, commercial, residential and institutional projects through a unified design, engineering and execution approach.",
           "Our MEPF capabilities are aligned with project requirements, applicable codes and best engineering practices to ensure safe, efficient, reliable and sustainable built environments."],
    cap_title='Our <span>Capabilities</span>', cap_sub="Integrated MEPF solutions across project types",
    caps=[
      ("bi-gear", "MEP Design &amp; Engineering", ["Integrated MEPF design", "BIM and coordinated 3D workflows", "System sizing and calculations", "Detailed drawings and documentation", "Value engineering and constructability review"]),
      ("bi-lightning-charge", "Electrical Systems", ["Power distribution systems", "Lighting systems (internal &amp; external)", "Cable trays, bus ducts and rising mains", "Earthing and lightning protection", "ELV systems (data, CCTV, access control, PA, BMS, etc.)", "Standby power integration (where in scope)"]),
      ("bi-fan", "HVAC Systems", ["VRF/VRV systems", "Chillers and chilled water systems", "Ventilation and fresh air systems", "Clean rooms and precision cooling (where in scope)", "Ducting, insulation and balancing", "Energy-efficient HVAC solutions"]),
      ("bi-droplet", "Plumbing &amp; Public Health", ["Water supply and distribution", "Drainage and sewage systems", "Rainwater harvesting systems (where in scope)", "STP and water treatment systems (where in scope)", "Pumping systems and storage tanks", "Plumbing fixtures and sanitary installations"]),
      ("bi-fire", "Fire Protection Systems", ["Fire detection and alarm systems", "Hydrant and sprinkler systems", "Fire pumps and associated systems", "Fire water storage and distribution", "Smoke control and pressurization systems (where in scope)", "Testing, commissioning and compliance documentation"]),
    ],
    approach=[("bi-diagram-3", "Integrated Design", "Coordinated MEPF design to eliminate clashes and improve efficiency."),
              ("bi-building-check", "Code-Compliant Solutions", "Design and execution as per applicable codes, standards and project requirements."),
              ("bi-cone-striped", "Quality Execution", "Skilled execution with robust QA/QC and testing procedures."),
              ("bi-tree", "Sustainable &amp; Efficient", "Energy and water-efficient solutions for long-term performance.")],
    approach_full=True,
    values=[("bi-house-heart", "Comfortable Spaces", "Well-designed systems for better living and working environments."),
            ("bi-gear", "Reliable Performance", "Efficient and dependable MEPF systems."),
            ("bi-currency-rupee", "Optimised Life-Cycle Cost", "Energy and water-efficient designs to reduce operating costs."),
            ("bi-tree", "Supports Green Building Certifications", "Aligned with sustainable and future-ready building practices.")],
    sectors=[("bi-building-gear", "Industrial"), ("bi-building", "Commercial"), ("bi-house-door", "Residential"), ("bi-bank", "Institutional")],
  ),
  dict(id="hvac", group="build", icon="bi-fan", img="service-hvac.jpg",
    name="HVAC Systems", title='HVAC <span>Systems</span>',
    short="VRF/VRV, chillers, ventilation, clean rooms and precision cooling for every building type.",
    mega="VRF, chillers, clean rooms, precision cooling",
    tagline="Comfort · Efficiency · Sustainability",
    quote="Advanced HVAC solutions for a healthier and more efficient tomorrow.",
    intro=["KALAGNI Integrated Projects Private Limited delivers integrated HVAC solutions for commercial, industrial, institutional and healthcare projects, designed for energy efficiency, indoor air quality and long-term performance.",
           "Our approach combines advanced engineering, quality systems and coordinated execution to ensure reliable and high-performance HVAC installations."],
    cap_title='Our <span>Capabilities</span>', cap_sub="Integrated HVAC solutions across project types",
    caps=[
      ("bi-fan", "VRF / VRV Systems", ["Variable refrigerant flow systems", "Energy efficient and flexible design", "Multi-zone temperature control", "Suitable for commercial and residential applications"]),
      ("bi-snow", "Chillers &amp; Chilled Water Systems", ["Water cooled and air cooled chillers", "Chilled water distribution systems", "Pumps, towers and piping", "Integration with building management systems"]),
      ("bi-wind", "Ventilation Systems", ["Fresh air and exhaust systems", "Air handling units (AHUs)", "Ducting and air distribution", "Indoor air quality compliance"]),
      ("bi-shield-plus", "Clean Rooms", ["Controlled environment design", "HEPA/ULPA filtration systems", "Pressure and temperature control", "Compliance with industry standards"]),
      ("bi-thermometer-snow", "Precision Cooling", ["Data centers and server rooms", "High precision temperature control", "Redundancy and reliability", "Energy efficient operation"]),
      ("bi-gear", "HVAC Design &amp; Execution", ["Load calculation and system design", "BIM and coordinated 3D workflows", "Installation, testing and commissioning", "Operation &amp; maintenance support"]),
    ],
    values=[("bi-tree", "Energy Efficiency", "Lower energy consumption and operating costs."),
            ("bi-wind", "Indoor Air Quality", "Healthier and more productive spaces."),
            ("bi-shield-check", "Reliable Performance", "Designed for durability and consistent operation."),
            ("bi-sliders", "Custom Solutions", "Tailored to project needs, space and usage."),
            ("bi-buildings", "Sustainable Buildings", "Supporting green and future-ready infrastructure.")],
    sectors=[("bi-building", "Commercial Buildings"), ("bi-building-gear", "Industrial Facilities"), ("bi-hospital", "Healthcare Facilities"), ("bi-mortarboard", "Educational Institutions"), ("bi-server", "Data Centers &amp; IT Spaces"), ("bi-tree", "Sustainable Buildings")],
  ),
  dict(id="railway-metro", group="build", icon="bi-train-front", img="service-railway-metro.jpg",
    name="Railway & Metro Infrastructure", title='Railway &amp; Metro <span>Infrastructure</span>',
    short="Electrification foundations, metro civil works, trackside works and associated electrical infrastructure.",
    mega="Electrification, metro &amp; trackside works",
    tagline="Connecting Cities · Powering Mobility · Building Tomorrow",
    quote="Infrastructure solutions for faster, safer and more connected communities.",
    intro=["KALAGNI delivers civil and electrical infrastructure solutions for railway and metro projects, supporting modern, efficient and sustainable transportation networks.",
           "Our capabilities include foundations, structural works, utility coordination and associated electrical infrastructure, executed in line with project requirements, standards and safety regulations."],
    cap_title='Our <span>Capabilities</span>', cap_sub="Civil and electrical infrastructure for railway and metro projects",
    caps=[
      ("bi-lightning", "Railway Electrification Infrastructure", ["Foundation works for railway electrification masts and poles", "Civil and structural foundation execution", "Site preparation, excavation and concreting", "Coordination with electrical and civil work packages"]),
      ("bi-train-front", "Metro Rail Infrastructure", ["Civil infrastructure and foundation works (viaducts, stations, depots, etc., subject to scope)", "Utility and site coordination", "Support for associated electrical infrastructure packages", "Coordination across multidisciplinary project interfaces"]),
      ("bi-sign-railroad", "Trackside Civil Works", ["Foundation and plinth works", "Cable route trenches and duct banks", "Drainage and associated civil works", "Retaining structures and access pathways", "Precision execution with quality control"]),
      ("bi-plug", "Associated Electrical Infrastructure", ["Traction power infrastructure (coordination, subject to scope)", "Cable routes and laying support", "Earthing and bonding systems", "Auxiliary power and lighting", "Testing, inspection and handover coordination (within awarded scope)"]),
      ("bi-cone-striped", "Project Execution Support", ["Planning and method statements", "Statutory and technical coordination", "Safety management and compliance", "Quality assurance and documentation", "Support for commissioning activities (within project scope)"]),
    ],
    values=[("bi-bullseye", "Sector Focus", "Understanding of railway and metro project requirements."),
            ("bi-shield-check", "Safe &amp; Quality", "Execution with strict safety and quality standards."),
            ("bi-gear", "Integrated Approach", "Coordination across civil, electrical and utility works."),
            ("bi-graph-up-arrow", "Reliable Execution", "Timely delivery with structured project management."),
            ("bi-tree", "Sustainable Infrastructure", "Supporting modern and low-carbon mobility solutions.")],
    sectors=[("bi-train-front", "Railways"), ("bi-train-lightrail-front", "Metro Rail"), ("bi-bricks", "Viaducts &amp; Stations"), ("bi-lightning-charge", "Traction Power"), ("bi-building", "Depots &amp; Yards"), ("bi-sign-railroad", "Trackside Works"), ("bi-stoplights", "Signalling &amp; Utilities")],
  ),
  dict(id="digital", group="support", icon="bi-cpu", img="service-digital.jpg",
    name="Engineering & Digital Solutions", title='Engineering &amp; <span>Digital Solutions</span>',
    short="ETAP studies, DIALux lighting, CAD &amp; BIM, SCADA/IoT, surveys and AI-enabled engineering.",
    mega="ETAP, BIM, SCADA / IoT, AI-enabled",
    tagline="Design · Analyze · Visualize · Optimize · Deliver",
    quote="Digital engineering for smarter, safer and more efficient infrastructure.",
    intro=["KALAGNI leverages advanced engineering tools and digital technologies to deliver accurate designs, optimized solutions and data-driven project execution across power, solar, buildings and infrastructure.",
           "Our engineering and digital capabilities enable better planning, coordination, asset performance and lifecycle management for sustainable and future-ready infrastructure."],
    cap_title='Our <span>Capabilities</span>', cap_sub="Technology-driven engineering solutions",
    caps=[
      ("bi-lightning-charge", "ETAP: Power System Studies", ["Load flow, short circuit and protection coordination", "Arc flash and motor starting studies", "Power system modeling and analysis", "Substation and distribution system studies", "Renewable and BESS integration studies (as applicable)"]),
      ("bi-lightbulb", "DIALux: Lighting Design", ["Lighting design and simulation", "Indoor and outdoor lighting layouts", "Daylight and energy analysis", "Compliance with relevant standards (as applicable)", "Optimized, energy-efficient lighting solutions"]),
      ("bi-box", "CAD &amp; BIM: Design &amp; Coordination", ["2D/3D CAD design and detailing", "BIM-based coordinated models", "Architectural, structural and MEPF integration", "Clash detection and conflict resolution", "Quantity take-off and documentation", "As-built modeling and digital handover"]),
      ("bi-display", "SCADA / IoT: Monitoring &amp; Control", ["SCADA system design and implementation", "IoT-enabled asset monitoring", "Real-time data acquisition and visualization", "Remote monitoring and control", "Integration with power, solar, BESS and building systems"]),
      ("bi-search", "Surveys &amp; Condition Monitoring", ["Thermal inspection and IR studies", "Asset condition assessment", "Drone surveys and 3D mapping", "Power quality and energy audits", "Predictive maintenance support", "Life extension and reliability improvement recommendations"]),
      ("bi-robot", "AI-Enabled Engineering", ["AI-assisted design optimization", "Data-driven performance analysis", "Predictive analytics for asset health", "Energy optimization and efficiency improvements", "Digital twins and smart infrastructure solutions (subject to project scope)"]),
    ],
    values=[("bi-gear", "Accurate Design", "Optimized and code-compliant engineering solutions."),
            ("bi-people", "Better Coordination", "Reduced clashes and rework through 3D workflows."),
            ("bi-bar-chart-line", "Higher Efficiency", "Energy-efficient and cost-optimized systems."),
            ("bi-database", "Data-Driven Decisions", "Real-time insights for better asset performance."),
            ("bi-tree", "Future-Ready", "Digital technologies for sustainable infrastructure.")],
    sectors=[("bi-lightning-charge", "Power Systems"), ("bi-sun", "Renewable Energy"), ("bi-buildings", "Buildings &amp; Infrastructure"), ("bi-gear", "Asset Management"), ("bi-bar-chart-line", "Digital Transformation"), ("bi-tree", "Sustainable Growth")],
  ),
  dict(id="approvals", group="support", icon="bi-clipboard-check", img="service-approvals.jpg",
    name="Approvals & Project Delivery", title='Approvals &amp; <span>Project Delivery</span>',
    short="Statutory approvals, utility coordination, land and regulatory support, PPA and grid connection.",
    mega="Statutory approvals &amp; utility coordination",
    tagline="Compliance · Coordination · Execution · Closure",
    quote="Clearances today for a smoother tomorrow.",
    intro=["KALAGNI provides end-to-end support for statutory approvals, utility coordination and project delivery, ensuring smooth execution from concept to commissioning. Our team works closely with government authorities, utilities and stakeholders to obtain necessary clearances and meet all applicable codes, standards and regulatory requirements.",
           "With structured project management processes, we ensure on-time, compliant and high-quality delivery across all project types."],
    cap_title='Our <span>Capabilities</span>', cap_sub="End-to-end support from approvals to commissioning",
    caps=[
      ("bi-bank", "Statutory Approvals", ["Building plan approvals", "Electrical &amp; fire NOCs", "Environmental clearances", "Pollution Control Board approvals (as applicable)", "Factory &amp; labour department coordination (as applicable)"]),
      ("bi-broadcast", "Utility Coordination", ["DISCOM / TGTRANSCO coordination (for power infrastructure)", "Load sanction and system studies", "Grid connection facilitation", "Metering and protection approvals", "Testing and commissioning clearances"]),
      ("bi-map", "Land &amp; Regulatory Support", ["Land due diligence support", "Land use and zoning clearances", "Conversion and layout approvals (as applicable)", "Coordination with local authorities", "Support for special approvals (as per project type)"]),
      ("bi-file-earmark-text", "PPA &amp; Grid Connection Support", ["Support in PPA process (for solar / renewable projects)", "Grid connection application and follow-up", "Technical documentation support", "Coordination with utilities and regulatory bodies"]),
      ("bi-shield-check", "Codes, Standards &amp; Compliance", ["Adherence to IS, IEC and applicable national codes", "Compliance with NBC and local building bye-laws", "Safety, fire and environmental regulations", "Quality documentation and audit readiness"]),
      ("bi-kanban", "Project Delivery Management", ["Integrated project planning", "Milestone-based execution", "Multi-disciplinary coordination", "Vendor and subcontractor management", "Testing, commissioning and handover support"]),
    ],
    values=[("bi-clock-history", "Faster Approval Cycles", "Through proactive coordination and experience."),
            ("bi-gear", "Reduced Execution Risk", "With compliance-driven planning."),
            ("bi-bar-chart-line", "Smoother Utility Interactions", "Strong relationships and documented processes."),
            ("bi-shield-check", "Regulatory Compliance", "As per applicable laws, codes and standards."),
            ("bi-people", "End-to-End Support", "From approvals to successful commissioning.")],
    sectors=[("bi-bank", "Government Authorities"), ("bi-broadcast", "Power Utilities"), ("bi-buildings", "Local Bodies"), ("bi-tree", "Environmental Authorities"), ("bi-file-earmark-text", "Regulatory Compliance"), ("bi-people", "Project Stakeholders")],
  ),
  dict(id="om", group="support", icon="bi-tools", img="service-om.jpg",
    name="Operations & Maintenance", title='Operations &amp; <span>Maintenance</span>',
    short="Electrical, solar, MEPF and facility O&amp;M with condition monitoring and long-term AMC support.",
    mega="Preventive maintenance, AMC &amp; monitoring",
    tagline="Maximum Uptime · Optimal Performance · Longer Asset Life",
    quote="Reliable operations for a more productive and sustainable tomorrow.",
    intro=["KALAGNI provides comprehensive operations and maintenance (O&amp;M) services for electrical, mechanical and civil infrastructure.",
           "Our O&amp;M approach focuses on reliability, safety, efficiency and cost optimization, supported by preventive maintenance, condition monitoring and digital tools to ensure continuous and trouble-free operations."],
    cap_title='Our <span>O&amp;M Services</span>', cap_sub="O&amp;M support across power, renewable, buildings and infrastructure assets",
    caps=[
      ("bi-lightning-charge", "Electrical Systems O&amp;M", ["HT/LT systems and substations", "Preventive and breakdown maintenance", "Electrical testing and diagnostics", "Protection system checks", "Power quality monitoring", "Energy efficiency improvements"]),
      ("bi-sun", "Solar &amp; BESS O&amp;M", ["Solar plant operations and monitoring", "Preventive and corrective maintenance", "Performance analysis and reporting", "BESS operations and health monitoring", "Inverter, transformer and auxiliary systems", "Remote monitoring and data analytics"]),
      ("bi-gear", "MEPF Systems O&amp;M", ["HVAC, plumbing and firefighting systems", "Equipment inspection and servicing", "Filter, chiller and pump maintenance", "Compliance with safety and industry standards", "Scheduled maintenance plans", "System performance optimization"]),
      ("bi-buildings", "Buildings &amp; Facilities O&amp;M", ["Facility management support", "Civil and architectural maintenance", "Electrical and MEPF upkeep", "Contract maintenance services", "Safety, compliance and housekeeping", "Asset lifecycle management"]),
      ("bi-display", "Condition Monitoring &amp; Digital O&amp;M", ["SCADA/IoT based monitoring", "Predictive maintenance programs", "Real-time asset health monitoring", "Data analytics and performance insights", "Remote support and diagnostics", "O&amp;M reporting and dashboards"]),
      ("bi-wrench-adjustable", "AMC &amp; Long-Term Support", ["Annual maintenance contracts", "Customized O&amp;M solutions", "Skilled manpower deployment", "Spares and inventory management", "24/7 support (subject to agreement)", "Regulatory and safety compliance"]),
    ],
    values=[("bi-gear", "Higher Uptime", "Reliable and continuous operations."),
            ("bi-bar-chart-line", "Lower Operating Cost", "Optimized performance and efficiency."),
            ("bi-shield-check", "Enhanced Safety", "Compliant and secure operations."),
            ("bi-tree", "Longer Asset Life", "Planned maintenance and proactive care."),
            ("bi-people", "Customized Support", "Solutions tailored to project needs.")],
    sectors=[("bi-lightning-charge", "Power Infrastructure"), ("bi-sun", "Renewable Energy"), ("bi-buildings", "Buildings &amp; Facilities"), ("bi-gear", "MEPF Systems"), ("bi-fan", "HVAC Systems"), ("bi-display", "Digital Monitoring"), ("bi-wrench-adjustable", "AMC &amp; O&amp;M Services")],
  ),
]
SVC = {s["id"]: s for s in SERVICES}

HIGHLIGHTS = [("bi-gear", "Integrated EPC Capabilities"), ("bi-shield-check", "Quality, Safety &amp; Compliance"),
              ("bi-people", "Experienced Leadership Team"), ("bi-bar-chart-line", "Client-Focused Execution"),
              ("bi-tree", "Sustainable Growth")]
STRENGTHS = [("bi-cone-striped", "Multi-Disciplinary Expertise"), ("bi-bullseye", "End-to-End Project Delivery"),
             ("bi-people-fill", "Client-Centric Approach"), ("bi-tree-fill", "Commitment to Sustainability")]
VALUES = [("bi-shield-check", "Safety First", "A safe workplace for our people, partners and communities."),
          ("bi-patch-check", "Quality Driven", "Consistent quality in design, materials and execution."),
          ("bi-people", "Integrity", "Transparent, ethical and responsible in all our actions."),
          ("bi-lightbulb", "Innovation", "Adopting advanced technologies for smarter and more efficient solutions."),
          ("bi-tree", "Sustainability", "Building for a cleaner, greener and more resilient tomorrow."),
          ("bi-bar-chart-line", "Client Success", "Delivering long-term value through reliable execution and strong partnerships.")]
WORKFLOW = [("bi-pencil-square", "Concept Design"), ("bi-gear", "Custom Engineering"),
            ("bi-clipboard-check", "Statutory Approvals Coordination"), ("bi-cart3", "Procurement Coordination"),
            ("bi-cone-striped", "Installation &amp; Execution"), ("bi-tools", "Testing &amp; Commissioning"),
            ("bi-file-earmark-text", "Handover &amp; Documentation"), ("bi-arrow-repeat", "AMC &amp; Lifecycle Support")]
SECTORS = [("electrical", "bi-lightning-charge", "Power Infrastructure"), ("solar-bess", "bi-sun", "Renewable Energy"),
           ("infrastructure", "bi-buildings", "Buildings &amp; Construction"), ("mepf", "bi-fan", "MEPF &amp; HVAC"),
           ("railway-metro", "bi-train-front", "Railway &amp; Metro"), ("digital", "bi-cpu", "Digital Solutions"),
           ("om", "bi-tools", "Operations &amp; Maintenance")]
CERTS = [("ISO<small>9001:2015</small>", "ISO 9001:2015", "Quality Management"),
         ("ISO<small>14001:2015</small>", "ISO 14001:2015", "Environmental Management"),
         ("ISO<small>45001:2018</small>", "ISO 45001:2018", "Occupational Health &amp; Safety"),
         ('<i class="bi bi-bank" aria-hidden="true"></i>', "MSME", "Registered"),
         ('<i class="bi bi-clipboard-check" aria-hidden="true"></i>', "Statutory Compliances", "As applicable")]
LEADERS = [
  dict(icon="bi-gear", name="Chethan Kumar", role="Director, Engineering &amp; Technical Solutions", tag="The Technical Solutions Leader",
       edu="Graduate in Electrical Engineering",
       exp="10+ years as a Senior Design Engineer. Experience with GE Vernova, ABB and Siemens in engineering design and EPC project delivery.",
       at="Oversees engineering coordination, technical solutions, design delivery and quality assurance."),
  dict(icon="bi-people-fill", name="Manikanta Jillagoni", role="Founder | Director, Operations &amp; Business Support", tag="The Vision &amp; Operations Driver",
       edu="Graduate in Electrical and Electronics Engineering",
       exp="Operations-led leader with experience in strategy, business development, government liaison, client relationships and power infrastructure. Connects technical planning with field execution.",
       at="Leads overall operations, business support, government liaison, client management, tender leadership and integrated EPC growth."),
  dict(icon="bi-cone-striped", name="Vinay Kumar Reddy", role="Director, Project Execution &amp; Infrastructure", tag="The Project Delivery Leader",
       edu="Graduate in Mechanical Engineering",
       exp="7+ years in execution of electrical, civil and MEPF works. Hands-on experience in project planning, site execution and handover.",
       at="Responsible for project planning, site execution, quality control, safety and timely project delivery."),
  dict(icon="bi-buildings", name="Aravind Reddy", role="Executive Director | Engineering, Construction &amp; Infrastructure", tag="The Client &amp; Business Development Leader", dark=True,
       edu="Graduate in Electrical and Electronics Engineering",
       exp="A veteran engineering professional with 25 years of experience spanning engineering, construction and infrastructure. Brings practical field knowledge to project planning, multidisciplinary coordination and delivery.",
       at="Leads client engagement, business development and stakeholder coordination, aligning client requirements with project objectives and business growth opportunities."),
  dict(icon="bi-graph-up-arrow", name="Vinod Duram", role="Executive Director | Corporate Strategy &amp; Finance", tag="The Strategy, Finance &amp; Business Development Leader", dark=True,
       confirm="CONFIRM before publishing: name spelled 'Vinod Duram' here but 'Dr. Vinod Durgam' on the infrastructure slide; company 'Busikem Indian Construction' here but 'BrickCem Construction Private Limited' there.",
       edu="Doctorate in Marketing",
       exp="20+ years with TCS as Cluster Head &amp; Delivery Lead handling large-scale projects and business operations. 10+ years as owner of Busikem Indian Construction with expertise in construction and infrastructure.",
       at="Leads financial planning, corporate governance, strategic partnerships and business development."),
]
ORG_GROUPS = [
  ("bi-lightning-charge", "EPC &amp; Power Infrastructure", ["L&amp;T Construction", "Tata Projects", "Siemens", "GE Vernova", "ABB", "Schneider Electric"]),
  ("bi-server", "Data Centers &amp; IT Infrastructure", ["TCS", "Tech Mahindra", "NTT Global Data Centers", "STT GDC India", "Capgemini"]),
  ("bi-building-gear", "Industrial &amp; Manufacturing", ["Maruti Suzuki", "Dr. Reddy's", "Aurobindo", "ITC Limited"]),
  ("bi-buildings", "Commercial Real Estate &amp; Developers", ["DLF", "Prestige Group", "Embassy Group", "Aparna", "My Home Group", "Vamsiram", "SMR Holdings", "Muppa", "Orange Constructions"]),
  ("bi-sun", "Renewable Energy", ["Adani Green Energy", "Tata Power Solar"]),
  ("bi-heart-pulse", "Healthcare &amp; Diagnostics", ["Vijaya Diagnostic Centre"]),
]
GOV = [("GHMC", "Greater Hyderabad Municipal Corporation"), ("HMDA", "Hyderabad Metropolitan Development Authority"),
       ("TGSICCL", "Telangana State Industrial Infrastructure Corporation Limited"), ("TGSPDCL", "Telangana Southern Power Distribution Company Limited"),
       ("TGNPDCL", "Telangana Northern Power Distribution Company Limited"), ("TGTRANSCO", "Telangana State Transmission Corporation Limited"),
       ("TSGENCO", "Telangana State Power Generation Corporation Limited"), ("R&amp;B", "Roads &amp; Buildings Department, Government of Telangana"),
       ("TGREDCO", "Telangana Renewable Energy Development Corporation Limited"), ("Mission Bhagiratha", "Drinking Water Supply Project, Government of Telangana"),
       ("Indian Railways", "South Central Railway"), ("APSPDCL", "Andhra Pradesh Southern Power Distribution Company Limited"),
       ("APTRANSCO", "Andhra Pradesh Transmission Corporation Limited"), ("KPTCL", "Karnataka Power Transmission Corporation Limited"),
       ("BESCOM", "Bangalore Electricity Supply Company Limited"), ("GESCOM", "Gulbarga Electricity Supply Company Limited")]
STRENGTH_EXP = [("bi-shield-check", "Multi-Sector Exposure", "Across power, infrastructure, industrial and commercial sectors."),
                ("bi-people", "Proven Execution Capability", "Delivered complex projects through experienced leadership."),
                ("bi-gear", "Strong Industry Relationships", "Trusted by leading organizations and public sector entities."),
                ("bi-bar-chart-line", "Knowledge Transfer to KALAGNI", "Applying best practices and experience to deliver value.")]
WHY_PARTNER = [("bi-gear", "Integrated Capabilities", "Multi-disciplinary EPC."), ("bi-person-check", "Experienced Leadership", "Sector expertise."),
               ("bi-shield-check", "Reliable Execution", "Quality and safety focus."), ("bi-people", "Client-Centric Approach", "Flexible and responsive."),
               ("bi-bar-chart-line", "Long-Term Partnership", "Committed to your success.")]

# =====================================================================
# SMALL BUILDING BLOCKS
# =====================================================================
def i(icon):
    return f'<i class="bi {icon}" aria-hidden="true"></i>'

def media(img, icon, ratio="4x3", extra="", alt=""):
    role = f' role="img" aria-label="{alt}"' if alt else ' aria-hidden="true"'
    return (f'<div class="media media-{ratio} {extra}" data-img="~R~assets/images/{img}"{role}>'
            f'<span class="media-icon">{i(icon)}</span><span class="media-label">{img}</span></div>')

def head(eyebrow, title, sub=None, center=True, tag="h2", title_id=None):
    cls = "section-head text-center" if center else "section-head"
    idattr = f' id="{title_id}"' if title_id else ""
    s = f'<div class="{cls}">\n'
    s += f'          <p class="eyebrow">{eyebrow}</p>\n'
    s += f'          <{tag} class="section-title heading-accent"{idattr}>{title}</{tag}>\n'
    if sub:
        s += f'          <p class="section-sub">{sub}</p>\n'
    s += '        </div>'
    return s

def quote_btn(label="Get a Quote", cls="btn btn-gold btn-pill", service=None, size=""):
    ds = f' data-service="{esc(service)}"' if service else ""
    return (f'<button type="button" class="{cls} {size}" data-bs-toggle="modal" data-bs-target="#quoteModal"{ds}>'
            f'{i("bi-send")} {label}</button>')

def value_strip(values):
    n = len(values)
    items = "\n".join(
        f'''              <div class="col"><div class="vp-item"><span class="icon-outline">{i(ic)}</span>
                <div><p class="vp-title">{t}</p><p class="vp-text">{txt}</p></div></div></div>'''
        for ic, t, txt in values)
    return f'''
        <div class="value-strip mt-4">
          <div class="row g-4 align-items-center">
            <div class="col-xl-2">
              <p class="value-strip-label mb-0"><span class="icon-ring icon-ring-sm">{i("bi-bullseye")}</span><span class="vsl-text">Our Value <br class="d-none d-xl-inline"><span>Proposition</span></span></p>
            </div>
            <div class="col-xl-10">
              <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-{n} g-3">
{items}
              </div>
            </div>
          </div>
        </div>'''

def value_statement(text):
    return f'''
        <div class="value-strip mt-4">
          <div class="row g-3 align-items-center">
            <div class="col-lg-3">
              <p class="value-strip-label mb-0"><span class="icon-ring icon-ring-sm">{i("bi-bullseye")}</span><span class="vsl-text">Our Value <span>Proposition</span></span></p>
            </div>
            <div class="col-lg-9"><p class="mb-0 fw-medium">{text}</p></div>
          </div>
        </div>'''

def sector_strip(items):
    spans = "".join(f'<span>{i(ic)}{t}</span>' for ic, t in items)
    return f'\n        <div class="sector-strip mt-4">{spans}</div>'

def approach_panel(items, full=False):
    col = "col-md-6 col-xl-3" if full else "col-md-6"
    rows = "\n".join(
        f'''              <div class="{col}"><div class="approach-item"><span class="icon-ring icon-ring-sm">{i(ic)}</span>
                <div><h4>{t}</h4><p>{txt}</p></div></div></div>''' for ic, t, txt in items)
    return f'''<div class="approach">
            <h3 class="sub-title mb-4">Our <span>Approach</span></h3>
            <div class="row g-4">
{rows}
            </div>
          </div>'''

def info_panel(p):
    lst_cls = "check-list row row-cols-1 row-cols-sm-2 g-0" if p.get("two_col") else "check-list"
    li_wrap = (lambda x: f'<li class="col">{i("bi-check2-circle")}<span>{x}</span></li>') if p.get("two_col") else \
              (lambda x: f'<li>{i("bi-check2-circle")}<span>{x}</span></li>')
    items = "".join(li_wrap(x) for x in p["items"])
    confirm = f'\n            <!-- {p["confirm"]} -->' if p.get("confirm") else ""
    note = f'<p class="note">{p["note"]}</p>' if p.get("note") else ""
    return f'''<div class="info-panel">{confirm}
            <div class="d-flex align-items-center gap-3 mb-3"><span class="icon-ring icon-ring-sm">{i(p["icon"])}</span>
              <h3 class="sub-title heading-accent mb-0 fs-5">{p["title"]}</h3></div>
            <p>{p["text"]}</p>
            <ul class="{lst_cls}">{items}</ul>{note}
          </div>'''

def cap_card(n, icon, title, items):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'''          <div class="col">
            <article class="cap-card lift">
              <div class="cap-card-head"><span class="cap-num">{n:02d}</span><h4>{title}</h4><span class="icon-ring icon-ring-sm">{i(icon)}</span></div>
              <ul class="cap-list">{lis}</ul>
            </article>
          </div>'''

def service_card(n, s):
    return f'''          <div class="col">
            <a class="service-card lift" href="~P~services.html#{s["id"]}">
              <div class="service-card-media">{media(s["img"], s["icon"], "16x9")}<span class="service-num">{n:02d}</span></div>
              <div class="service-card-body">
                <span class="icon-ring">{i(s["icon"])}</span>
                <h3>{s["title"].replace("<span>", "").replace("</span>", "")}</h3>
                <p>{s["short"]}</p>
                <span class="more">Learn more {i("bi-arrow-right")}</span>
              </div>
            </a>
          </div>'''

def certs_section(cls="section section-soft"):
    items = "\n".join(f'''          <div class="col"><div class="cert"><div class="cert-badge">{b}</div>
            <p class="cert-title">{t}</p><p class="cert-sub">{sub}</p></div></div>''' for b, t, sub in CERTS)
    return f'''
    <!-- ================= CERTIFICATIONS ================= -->
    <section class="{cls}" aria-labelledby="certs-title">
      <div class="container">
        {head("Quality · Environment · Safety", 'Certifications &amp; <span>Compliance</span>', title_id="certs-title")}
        <div class="row row-cols-2 row-cols-md-3 row-cols-lg-5 g-4 justify-content-center">
{items}
        </div>
      </div>
    </section>
'''

def values_section(cls="section section-soft", sid="values"):
    cards = "\n".join(f'''          <div class="col"><article class="value-card lift"><span class="icon-ring">{i(ic)}</span>
            <h3>{t}</h3><p>{txt}</p></article></div>''' for ic, t, txt in VALUES)
    return f'''
    <!-- ================= VALUES ================= -->
    <section class="{cls}" id="{sid}" aria-labelledby="{sid}-title">
      <div class="container">
        {head("The foundation of everything we do", 'Our <span>Values</span>', title_id=sid + "-title")}
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
{cards}
        </div>
      </div>
    </section>
'''

def strengths_band():
    items = "\n".join(f'          <div class="col"><div class="band-item">{i(ic)}<span>{t}</span></div></div>' for ic, t in STRENGTHS)
    return f'''
    <!-- ================= STRENGTHS BAND ================= -->
    <section class="band" aria-label="Our strengths">
      <div class="container">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 g-4">
{items}
        </div>
      </div>
    </section>
'''

def workflow_section(sid="workflow"):
    steps = "\n".join(f'''          <li class="col"><div class="step"><span class="step-num">{n:02d}</span>
            <span class="icon-ring">{i(ic)}</span><span class="step-label">{t}</span></div></li>'''
                      for n, (ic, t) in enumerate(WORKFLOW, 1))
    return f'''
    <!-- ================= DELIVERY WORKFLOW ================= -->
    <section class="section section-navy" id="{sid}" aria-labelledby="{sid}-title">
      <div class="container">
        {head("A coordinated EPC approach for reliable project delivery", 'Our <span>Delivery Workflow</span>', "From concept to commissioning: one coordinated process, one accountable partner.", title_id=sid + "-title")}
        <ol class="row row-cols-2 row-cols-md-4 row-cols-xl-8 g-3 workflow list-unstyled mb-0">
{steps}
        </ol>
      </div>
    </section>
'''

def who_section(full=False):
    hl = "\n".join(f'              <li><span class="icon-ring icon-ring-sm">{i(ic)}</span>{t}</li>' for ic, t in HIGHLIGHTS)
    btn = "" if full else f'\n            <a class="btn btn-outline-navy btn-pill mt-4" href="~P~about.html">More about us {i("bi-arrow-right")}</a>'
    return f'''
    <!-- ================= WHO WE ARE ================= -->
    <section class="section" id="who-we-are" aria-labelledby="who-title">
      <div class="container">
        <div class="row g-5 align-items-center">
          <div class="col-lg-5">
            <p class="eyebrow">Who we are</p>
            <h2 class="section-title heading-accent" id="who-title">Who <span>We Are</span></h2>
            <p class="tagline-spaced mb-4">Integrated Solutions | Reliable Execution</p>
            <div class="lead-border">
              <p>KALAGNI Integrated Projects Private Limited is an integrated EPC contractor delivering end-to-end solutions across Power, Infrastructure, MEPF, HVAC and Digital Engineering. We bring together engineering expertise, execution excellence and project management discipline to deliver reliable, sustainable and future-ready infrastructure for our clients.</p>
              <p>With a multi-disciplinary team and a collaborative approach, we take projects from concept to commissioning, ensuring quality, safety, on-time delivery and long-term value.</p>
            </div>{btn}
          </div>
          <div class="col-md-6 col-lg-3">
            <ul class="highlight-list">
{hl}
            </ul>
          </div>
          <div class="col-md-6 col-lg-4">
            <div class="slant-frame">{media("about.jpg", "bi-buildings", "4x3", "media-slant", "KALAGNI office building")}</div>
            <p class="side-quote mt-4 mb-0">People Driving Possibilities</p>
          </div>
        </div>
      </div>
    </section>
'''

def banner(img, crumb, eyebrow, title, lead):
    return f'''
    <!-- ================= PAGE BANNER ================= -->
    <section class="page-banner" data-img="~R~assets/images/{img}">
      <div class="container">
        <nav aria-label="Breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="~R~index.html">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">{crumb}</li>
          </ol>
        </nav>
        <p class="eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        <p class="lead mb-0">{lead}</p>
      </div>
    </section>
'''

# =====================================================================
# SHARED: HEAD + NAVBAR / CTA + FOOTER + FLOATING BUTTONS + MODAL
# =====================================================================
def mega_items(group):
    out = []
    for s in SERVICES:
        if s["group"] != group: continue
        out.append(f'''                        <li>
                          <a class="mega-link" href="~P~services.html#{s["id"]}">
                            <span class="mega-icon">{i(s["icon"])}</span>
                            <span><span class="mega-title">{s["title"].replace("<span>", "").replace("</span>", "")}</span><span class="mega-desc">{s["mega"]}</span></span>
                          </a>
                        </li>''')
    return "\n".join(out)

HEADER = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{TITLE}</title>
  <meta name="description" content="{DESC}">
  <meta name="theme-color" content="#011c3a">

  <link rel="icon" type="image/png" href="~R~assets/images/favicon.png">
  <link rel="apple-touch-icon" href="~R~assets/images/apple-touch-icon.png">

  <!-- 1. Bootstrap CSS, then Bootstrap Icons (local copies) -->
  <link rel="stylesheet" href="~R~vendor/bootstrap/bootstrap.min.css">
  <link rel="stylesheet" href="~R~vendor/bootstrap-icons/bootstrap-icons.min.css">

  <!-- 2. Our own CSS (after Bootstrap, so our styles win) -->
  <link rel="stylesheet" href="~R~css/style.css">
</head>
<body>

  <a class="skip-link visually-hidden-focusable" href="#main">Skip to main content</a>

  <!-- ================= TOP BAR ================= -->
  <div class="topbar">
    <div class="container d-flex align-items-center justify-content-center justify-content-lg-between gap-3 py-2">
      <p class="topbar-tagline mb-0 d-none d-lg-block">Integrated Engineering. Reliable Execution.</p>
      <ul class="list-unstyled d-flex align-items-center gap-3 gap-md-4 mb-0">
        <li><a href="tel:PHONE_TEL"><i class="bi bi-telephone-fill" aria-hidden="true"></i>PHONE_DISPLAY</a></li>
        <li class="d-none d-sm-block"><a href="mailto:EMAIL"><i class="bi bi-envelope-fill" aria-hidden="true"></i>EMAIL</a></li>
        <li class="d-none d-md-block"><i class="bi bi-patch-check-fill" aria-hidden="true"></i>ISO 9001 · 14001 · 45001</li>
      </ul>
    </div>
  </div>

  <!-- ================= NAVBAR =================
       navbar-expand-xl : full menu from 1200px, hamburger below
       sticky-top       : stays at the top while scrolling
       offcanvas-start  : on mobile the menu slides in from the left -->
  <nav class="navbar navbar-expand-xl site-navbar sticky-top" aria-label="Main navigation">
    <div class="container">

      <a class="navbar-brand brand" href="~R~index.html">
        <img class="brand-logo" src="~R~assets/images/logo-white.png" alt="KALAGNI Integrated Projects Private Limited" width="574" height="185">
      </a>

      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#mainNav" aria-controls="mainNav" aria-label="Open menu">
        <i class="bi bi-list" aria-hidden="true"></i>
      </button>

      <div class="offcanvas offcanvas-start" tabindex="-1" id="mainNav" aria-labelledby="mainNavLabel">

        <!-- Only visible on mobile (Bootstrap hides it from 1200px) -->
        <div class="offcanvas-header">
          <img class="brand-logo" id="mainNavLabel" src="~R~assets/images/logo-white.png" alt="KALAGNI menu" width="574" height="185">
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close menu"></button>
        </div>

        <div class="offcanvas-body align-items-xl-center">
          <ul class="navbar-nav flex-grow-1 justify-content-xl-center">

            <li class="nav-item">
              <a class="nav-link{ACT_home}" href="~R~index.html">Home</a>
            </li>

            <!-- Menu order follows the visitor: what you do -> proof -> who you are -> contact -->

            <!-- Services: MEGA MENU. "position-static" lets the menu stretch across the whole navbar -->
            <li class="nav-item dropdown position-static">
              <a class="nav-link dropdown-toggle{CLS_services}" href="~P~services.html" role="button" data-bs-toggle="dropdown" aria-expanded="false">Services</a>
              <div class="dropdown-menu mega-menu">
                <div class="container">
                  <div class="row g-4">

                    <div class="col-xl-3">
                      <p class="mega-heading">Power &amp; Energy</p>
                      <ul class="list-unstyled mb-0">
{ITEMS_power}
                      </ul>
                    </div>

                    <div class="col-xl-3">
                      <p class="mega-heading">Buildings &amp; Infrastructure</p>
                      <ul class="list-unstyled mb-0">
{ITEMS_build}
                      </ul>
                    </div>

                    <div class="col-xl-3">
                      <p class="mega-heading">Engineering &amp; Support</p>
                      <ul class="list-unstyled mb-0">
{ITEMS_support}
                      </ul>
                      <a class="mega-all d-xl-none" href="~P~services.html">View all services <i class="bi bi-arrow-right" aria-hidden="true"></i></a>
                    </div>

                    <!-- Promo card: desktop only -->
                    <div class="col-xl-3 d-none d-xl-block">
                      <div class="mega-promo">
                        <p class="eyebrow">From concept to commissioning</p>
                        <p class="mega-promo-title">Integrated <span>EPC Solutions</span></p>
                        <p>One partner for engineering, approvals, execution and lifecycle support.</p>
                        <a class="btn btn-gold btn-sm" href="~P~services.html">View all services <i class="bi bi-arrow-right" aria-hidden="true"></i></a>
                      </div>
                    </div>

                  </div>
                </div>
              </div>
            </li>

            <li class="nav-item">
              <a class="nav-link{ACT_clients}" href="~P~clients.html">Clients</a>
            </li>

            <!-- About: small dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle{CLS_about}" href="~P~about.html" role="button" data-bs-toggle="dropdown" aria-expanded="false">About</a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="~P~about.html#who-we-are">Who We Are</a></li>
                <li><a class="dropdown-item" href="~P~about.html#values">Our Values</a></li>
                <li><a class="dropdown-item" href="~P~about.html#leadership">Leadership Team</a></li>
              </ul>
            </li>

            <li class="nav-item">
              <a class="nav-link{ACT_contact}" href="~P~contact.html">Contact</a>
            </li>
          </ul>

          <!-- Action buttons: stacked in the mobile menu, side by side on desktop -->
          <div class="d-flex flex-column flex-xl-row gap-2 mt-4 mt-xl-0 ms-xl-3">
            <a class="btn btn-outline-gold btn-pill btn-sm px-3" href="~R~assets/docs/kalagni-profile.pdf" download>
              <i class="bi bi-file-earmark-pdf" aria-hidden="true"></i> Company Profile
            </a>
            <button type="button" class="btn btn-gold btn-pill btn-sm px-3" data-bs-toggle="modal" data-bs-target="#quoteModal">
              <i class="bi bi-send" aria-hidden="true"></i> Get a Quote
            </button>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <main id="main">
"""

CTA = """
    <!-- ================= CALL TO ACTION ================= -->
    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container">
        <div class="row align-items-center g-4">
          <div class="col-lg-8">
            <p class="eyebrow">Discuss · Partner · Plan · Execute · Grow</p>
            <h2 class="section-title mb-2" id="cta-title">Let's Build a <span>Stronger Tomorrow</span> Together</h2>
            <p class="mb-0">KALAGNI is ready to partner with clients, consultants and institutions to deliver reliable, future-ready infrastructure across power, renewable energy, buildings and beyond.</p>
          </div>
          <div class="col-lg-4 d-flex flex-wrap gap-2 justify-content-lg-end">
            QUOTE_BTN
            <a class="btn btn-outline-gold btn-pill btn-lg" href="tel:PHONE_TEL"><i class="bi bi-telephone" aria-hidden="true"></i> Call Us</a>
          </div>
        </div>
      </div>
    </section>
"""

def form_html(p):
    opts = "".join(f'<option value="{esc(s["name"])}">{esc(s["name"])}</option>' for s in SERVICES)
    return f'''<form class="js-enquiry-form" novalidate>
          <div class="row g-3">
            <div class="col-md-6">
              <label for="{p}-name" class="form-label">Full name <span class="req" aria-hidden="true">*</span></label>
              <input type="text" class="form-control" id="{p}-name" name="name" autocomplete="name" required>
              <div class="invalid-feedback">Please enter your name.</div>
            </div>
            <div class="col-md-6">
              <label for="{p}-company" class="form-label">Company</label>
              <input type="text" class="form-control" id="{p}-company" name="company" autocomplete="organization">
            </div>
            <div class="col-md-6">
              <label for="{p}-email" class="form-label">Email <span class="req" aria-hidden="true">*</span></label>
              <input type="email" class="form-control" id="{p}-email" name="email" autocomplete="email" required>
              <div class="invalid-feedback">Please enter a valid email address.</div>
            </div>
            <div class="col-md-6">
              <label for="{p}-phone" class="form-label">Phone <span class="req" aria-hidden="true">*</span></label>
              <input type="tel" class="form-control" id="{p}-phone" name="phone" autocomplete="tel" pattern="[0-9+ \\-]{{8,20}}" required>
              <div class="invalid-feedback">Please enter a valid phone number.</div>
            </div>
            <div class="col-md-6">
              <label for="{p}-service" class="form-label">Service required <span class="req" aria-hidden="true">*</span></label>
              <select class="form-select" id="{p}-service" name="service" required>
                <option value="" selected disabled>Select a service</option>{opts}<option value="Other / multiple services">Other / multiple services</option>
              </select>
              <div class="invalid-feedback">Please choose a service.</div>
            </div>
            <div class="col-md-6">
              <label for="{p}-location" class="form-label">Project location</label>
              <input type="text" class="form-control" id="{p}-location" name="location" autocomplete="address-level2">
            </div>
            <div class="col-12">
              <label for="{p}-message" class="form-label">Project details <span class="req" aria-hidden="true">*</span></label>
              <textarea class="form-control" id="{p}-message" name="message" rows="4" required></textarea>
              <div class="invalid-feedback">Please describe your requirement briefly.</div>
            </div>
            <div class="col-12">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" id="{p}-consent" name="consent" required>
                <label class="form-check-label small" for="{p}-consent">I agree to be contacted by KALAGNI about this enquiry.</label>
                <div class="invalid-feedback">Please confirm so we can contact you.</div>
              </div>
            </div>
            <div class="col-12">
              <button type="submit" class="btn btn-gold btn-pill btn-lg px-4"><i class="bi bi-send" aria-hidden="true"></i> Send Enquiry</button>
            </div>
          </div>
          <div class="form-success alert alert-success mt-3 mb-0" role="status" tabindex="-1">
            <i class="bi bi-check-circle-fill" aria-hidden="true"></i> Thank you! Your enquiry has been noted. Our team will get back to you shortly.
          </div>
        </form>'''

FOOTER = """
  </main>
CTA_BLOCK
  <!-- ================= FOOTER ================= -->
  <footer class="site-footer">
    <div class="footer-main">
      <div class="container">
        <div class="row g-5">
          <div class="col-md-6 col-xl-4">
            <a href="~R~index.html" class="d-inline-block mb-3">
              <img class="footer-logo" src="~R~assets/images/logo-white.png" alt="KALAGNI Integrated Projects Private Limited" width="574" height="185" loading="lazy">
            </a>
            <p>An integrated EPC contractor delivering end-to-end solutions across power, infrastructure, MEPF, HVAC and digital engineering, from concept to commissioning.</p>
            <ul class="footer-certs list-unstyled d-flex flex-wrap gap-2 mb-0">
              <li>ISO 9001:2015</li><li>ISO 14001:2015</li><li>ISO 45001:2018</li><li>MSME Registered</li>
            </ul>
          </div>

          <div class="col-sm-6 col-md-6 col-xl-2">
            <h2 class="footer-heading">Quick Links</h2>
            <ul class="footer-links">
              <li><a href="~R~index.html">Home</a></li>
              <li><a href="~P~services.html">Services</a></li>
              <li><a href="~P~clients.html">Clients</a></li>
              <li><a href="~P~about.html">About Us</a></li>
              <li><a href="~P~about.html#leadership">Leadership</a></li>
              <li><a href="~P~contact.html">Contact</a></li>
              <li><a href="~R~assets/docs/kalagni-profile.pdf" download>Company Profile (PDF)</a></li>
            </ul>
          </div>

          <div class="col-sm-6 col-md-6 col-xl-3">
            <h2 class="footer-heading">Our Services</h2>
            <ul class="footer-links">
FOOTER_SERVICES
            </ul>
          </div>

          <div class="col-md-6 col-xl-3">
            <h2 class="footer-heading">Get in Touch</h2>
            <ul class="footer-contact">
              <li><i class="bi bi-geo-alt-fill" aria-hidden="true"></i><span>Plot No. 59, Lumbini Avenue, Gachibowli, Serilingampally, K.V. Rangareddy, Telangana 500032, India</span></li>
              <li><i class="bi bi-telephone-fill" aria-hidden="true"></i><a href="tel:PHONE_TEL">PHONE_DISPLAY</a></li>
              <li><i class="bi bi-envelope-fill" aria-hidden="true"></i><a href="mailto:EMAIL">EMAIL</a></li>
              <li><i class="bi bi-whatsapp" aria-hidden="true"></i><a href="WHATSAPP" target="_blank" rel="noopener">Chat on WhatsApp</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Scrolling taglines (decorative, so hidden from screen readers) -->
    <div class="footer-marquee marquee" aria-hidden="true">
      <ul class="marquee-track">
MARQUEE
      </ul>
    </div>

    <div class="footer-bottom">
      <div class="container d-flex flex-column flex-md-row justify-content-between gap-2 text-center text-md-start">
        <p class="mb-0">&copy; <span class="js-year">2026</span> KALAGNI Integrated Projects Private Limited. All rights reserved.</p>
        <p class="mb-0">CIN: U42202TS2026PTC224342 · GSTIN: 36AANCK3239M1Z0</p>
      </div>
    </div>
  </footer>

  <!-- ================= FLOATING BUTTONS ================= -->
  <div class="float-actions">
    <a class="float-btn float-whatsapp" href="WHATSAPP" target="_blank" rel="noopener" aria-label="Chat on WhatsApp" data-label="Chat on WhatsApp"><i class="bi bi-whatsapp" aria-hidden="true"></i></a>
    <button type="button" class="float-btn float-quote" data-bs-toggle="modal" data-bs-target="#quoteModal" aria-label="Get a quote" data-label="Get a Quote"><i class="bi bi-send" aria-hidden="true"></i></button>
    <button type="button" class="float-btn float-top js-back-to-top" aria-label="Back to top" data-label="Back to top"><i class="bi bi-arrow-up" aria-hidden="true"></i></button>
  </div>

  <!-- ================= ENQUIRY POPUP (MODAL) ================= -->
  <div class="modal fade quote-modal" id="quoteModal" tabindex="-1" aria-labelledby="quoteModalTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <div>
            <p class="eyebrow mb-1">Discuss · Partner · Plan</p>
            <h2 class="modal-title h5 mb-0" id="quoteModalTitle">Request a Quote</h2>
          </div>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p class="small text-body-secondary">Tell us about your project and our team will get back to you. Prefer to talk? Call <a href="tel:PHONE_TEL">PHONE_DISPLAY</a> or <a href="WHATSAPP" target="_blank" rel="noopener">message us on WhatsApp</a>.</p>
          MODAL_FORM
        </div>
      </div>
    </div>
  </div>

  <!-- 3. Bootstrap JS bundle (local copy) -->
  <script src="~R~vendor/bootstrap/bootstrap.bundle.min.js"></script>
  <!-- 4. Our own JS -->
  <script src="~R~js/main.js"></script>
</body>
</html>
"""

def footer(cta=True):
    svc = "\n".join(f'              <li><a href="~P~services.html#{s["id"]}">{s["title"].replace("<span>", "").replace("</span>", "")}</a></li>' for s in SERVICES)
    tags = ["Integrated Engineering", "Reliable Execution", "From Concept to Commissioning", "People. Places. Progress.",
            "Powering a Brighter Tomorrow", "Youth Driven. Experience Backed."]
    marquee = "\n".join(f"        <li>{t}</li>" for t in tags + tags)
    f = FOOTER.replace("CTA_BLOCK", CTA.replace("QUOTE_BTN", quote_btn(size="btn-lg")) if cta else "")
    return (f.replace("FOOTER_SERVICES", svc).replace("MARQUEE", marquee)
             .replace("MODAL_FORM", form_html("q")))

# =====================================================================
# PAGES
# =====================================================================
HERO_SLIDES = [
  dict(img="hero-1.jpg", icon="bi-buildings", eyebrow="From concept to commissioning", tag="h1",
       title='Integrated <span>EPC Solutions</span>',
       text="Integrated engineering. Reliable execution. Power, infrastructure, MEPF, HVAC and digital engineering, delivered by one accountable partner.",
       primary=("Explore Services", "~P~services.html")),
  dict(img="hero-2.jpg", icon="bi-lightning-charge", eyebrow="Engineering · Execution · Testing · Commissioning", tag="h2",
       title='Electrical Power <span>Infrastructure</span>',
       text="HT/LT networks, GIS and AIS substations, underground cables and transmission lines, engineered and delivered according to the contracted scope.",
       primary=("Power Infrastructure", "~P~services.html#electrical")),
  dict(img="hero-3.jpg", icon="bi-sun", eyebrow="Clean energy · Reliable power · Sustainable growth", tag="h2",
       title='Solar &amp; <span>BESS Solutions</span>',
       text="End-to-end solar PV and battery energy storage, from design and grid connectivity to commissioning and O&amp;M.",
       primary=("Solar &amp; BESS", "~P~services.html#solar-bess")),
  dict(img="hero-4.jpg", icon="bi-building-gear", eyebrow="Plan · Design · Build · Deliver", tag="h2",
       title='Infrastructure &amp; <span>Construction</span>',
       text="Industrial, commercial and residential developments built through a planned, engineering-led and execution-focused approach.",
       primary=("Infrastructure &amp; Construction", "~P~services.html#infrastructure")),
]

def hero():
    ind = "\n".join(f'          <button type="button" data-bs-target="#heroCarousel" data-bs-slide-to="{n}"{" class=\"active\" aria-current=\"true\"" if n == 0 else ""} aria-label="Slide {n+1}"></button>' for n in range(len(HERO_SLIDES)))
    items = []
    for n, s in enumerate(HERO_SLIDES):
        items.append(f'''          <div class="carousel-item{" active" if n == 0 else ""}">
            <div class="hero-slide" data-img="~R~assets/images/{s["img"]}">
              {i(s["icon"]).replace('class="bi ', 'class="bi hero-art ')}
              <div class="container">
                <div class="hero-content">
                  <p class="eyebrow">{s["eyebrow"]}</p>
                  <{s["tag"]} class="hero-title">{s["title"]}</{s["tag"]}>
                  <p class="hero-text">{s["text"]}</p>
                  <div class="d-flex flex-wrap gap-2">
                    <a class="btn btn-gold btn-pill btn-lg" href="{s["primary"][1]}">{s["primary"][0]} {i("bi-arrow-right")}</a>
                    {quote_btn(cls="btn btn-outline-gold btn-pill", size="btn-lg")}
                  </div>
                </div>
              </div>
            </div>
          </div>''')
    items = "\n".join(items)
    return f'''
    <!-- ================= HERO CAROUSEL =================
         carousel-fade: slides fade into each other; data-bs-interval: 6 seconds per slide -->
    <section class="hero" aria-label="Featured services">
      <div id="heroCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel" data-bs-interval="6000">
        <div class="carousel-indicators">
{ind}
        </div>
        <div class="carousel-inner">
{items}
        </div>
        <button class="carousel-control-prev d-none d-lg-flex" type="button" data-bs-target="#heroCarousel" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="visually-hidden">Previous slide</span>
        </button>
        <button class="carousel-control-next d-none d-lg-flex" type="button" data-bs-target="#heroCarousel" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span><span class="visually-hidden">Next slide</span>
        </button>
        <button type="button" class="hero-pause" aria-label="Pause slideshow"><i class="bi bi-pause-fill" aria-hidden="true"></i></button>
      </div>
    </section>
'''

def home_main():
    cards = "\n".join(service_card(n, s) for n, s in enumerate(SERVICES, 1))
    sectors = "\n".join(f'''          <a class="sector" href="~P~services.html#{a}"><span class="sector-circle">{i(ic)}</span><span class="sector-label">{t}</span></a>''' for a, ic, t in SECTORS)
    names = [n for _, _, lst in ORG_GROUPS for n in lst]
    pills = "\n".join(f'            <li class="org-pill">{n}</li>' for n in names)
    pills_dup = "\n".join(f'            <li class="org-pill" aria-hidden="true">{n}</li>' for n in names)
    exp = "\n".join(f'''          <div class="col"><div class="vp-item"><span class="icon-outline">{i(ic)}</span>
            <div><p class="vp-title">{t}</p><p class="vp-text">{txt}</p></div></div></div>''' for ic, t, txt in STRENGTH_EXP)
    # Visitor journey: what do you do -> for which sectors -> how do you work
    # -> can I trust you -> who are you (short) -> contact (CTA band + footer)
    return (hero() + strengths_band() + f'''
    <!-- ================= SERVICES ================= -->
    <section class="section section-soft" id="services" aria-labelledby="services-title">
      <div class="container">
        {head("What we do", 'Our <span>Services</span>', "Nine integrated service lines across power, buildings and infrastructure, delivered by one accountable EPC partner.", title_id="services-title")}
        <div class="row row-cols-1 row-cols-md-2 row-cols-xl-3 g-4">
{cards}
        </div>
      </div>
    </section>

    <!-- ================= SECTORS ================= -->
    <section class="section" aria-labelledby="sectors-title">
      <div class="container">
        {head("Sectors we serve", 'Experienced <span>Across Sectors</span>', "Power, renewable energy, buildings, transport and digital: integrated EPC solutions for every stage of the asset lifecycle.", title_id="sectors-title")}
        <div class="d-flex flex-wrap justify-content-center gap-4">
{sectors}
        </div>
      </div>
    </section>
''' + workflow_section() + f'''
    <!-- ================= EXPERIENCE =================
         CONFIRM before publishing: per the company profile (slide 13), these are organizations
         associated with the LEADERSHIP TEAM, and references must be confirmed before publication.
         Names are shown as text; use logos only with permission. -->
    <section class="section" aria-labelledby="experience-title">
      <div class="container">
        {head("Trusted by leading organizations", 'Experience That <span>Builds Confidence</span>', "Our leadership team has been associated with reputed national and multinational organizations and public sector bodies across diverse sectors.", title_id="experience-title")}
      </div>
      <div class="marquee mb-5">
        <ul class="marquee-track">
{pills}
{pills_dup}
        </ul>
      </div>
      <div class="container">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 g-4">
{exp}
        </div>
        <div class="text-center mt-5">
          <a class="btn btn-outline-navy btn-pill" href="~P~clients.html">View clients &amp; experience {i("bi-arrow-right")}</a>
        </div>
      </div>
    </section>
''' + certs_section() + who_section())

def about_main():
    cards = []
    for n, L in enumerate(LEADERS):
        dark = L.get("dark")
        col = "col-md-6 col-lg-4" if n < 3 else "col-md-6 col-lg-5"
        confirm = f'\n            <!-- {L["confirm"]} -->' if L.get("confirm") else ""
        cards.append(f'''          <div class="{col}">{confirm}
            <article class="leader-card{" leader-card-dark" if dark else ""} lift">
              <div class="leader-head"><span class="icon-ring icon-ring-lg">{i(L["icon"])}</span>
                <div><h3 class="leader-name">{L["name"]}</h3><p class="leader-role">{L["role"]}</p></div></div>
              <span class="leader-tag">{L["tag"]}</span>
              <dl class="leader-facts">
                <dt>{i("bi-mortarboard")}Education</dt><dd>{L["edu"]}</dd>
                <dt>{i("bi-briefcase")}Professional Experience</dt><dd>{L["exp"]}</dd>
                <dt>{i("bi-bullseye")}At KALAGNI</dt><dd>{L["at"]}</dd>
              </dl>
            </article>
          </div>''')
    cards = "\n".join(cards)
    return (banner("banner-about.jpg", "About", "Integrated solutions | Reliable execution", 'About <span>KALAGNI</span>',
                   "An integrated EPC contractor with a multi-disciplinary team, taking projects from concept to commissioning.")
            # About order: our story -> the people behind it -> what we stand for -> certifications
            + who_section(full=True) + strengths_band() + f'''
    <!-- ================= LEADERSHIP ================= -->
    <section class="section" id="leadership" aria-labelledby="leadership-title">
      <div class="container">
        {head("Experience | Engineering | Execution", 'Leadership <span>Team</span>', "Our leadership combines deep technical expertise with proven engineering, construction, infrastructure and technology experience in private and government projects.", title_id="leadership-title")}
        <div class="row g-4 justify-content-center">
{cards}
        </div>
        <p class="tagline-spaced text-center mt-5 mb-0">Youth driven. Experience backed. <strong class="text-uppercase" style="color: var(--kg-gold-600)">KALAGNI.</strong></p>
      </div>
    </section>
''' + values_section(cls="section section-soft") + certs_section(cls="section"))

def services_main():
    jump = "\n".join(f'''          <div class="col"><a class="jump-card" href="#{s["id"]}"><span class="icon-ring icon-ring-sm">{i(s["icon"])}</span>
            <span><span class="jump-card-num">{n:02d}</span><span class="jump-card-title">{s["title"].replace("<span>", "").replace("</span>", "")}</span></span></a></div>''' for n, s in enumerate(SERVICES, 1))
    out = banner("banner-services.jpg", "Services", "Engineering | Execution | Commissioning", 'Our <span>Services</span>',
                 "Nine integrated service lines across power, renewable energy, buildings, transport and digital engineering, delivered by one accountable EPC partner.")
    out += f'''
    <!-- ================= ALL SERVICES (jump links) ================= -->
    <section class="section section-soft" id="all-services" aria-labelledby="all-services-title">
      <div class="container">
        {head("What we do", 'Integrated <span>EPC Solutions</span>', "Choose a service to jump straight to its details.", title_id="all-services-title")}
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-3">
{jump}
        </div>
      </div>
    </section>
'''
    for n, s in enumerate(SERVICES, 1):
        soft = " section-soft" if n % 2 == 0 else ""
        intro = "".join(f"<p>{p}</p>" for p in s["intro"])
        caps = "\n".join(cap_card(k, ic, t, items) for k, (ic, t, items) in enumerate(s["caps"], 1))
        extras = ""
        if s.get("approach") and s.get("panel"):
            extras = f'''
        <div class="row g-4 mt-1">
          <div class="col-lg-7">
          {approach_panel(s["approach"])}
          </div>
          <div class="col-lg-5">
          {info_panel(s["panel"])}
          </div>
        </div>'''
        elif s.get("approach"):
            extras = f'''
        <div class="mt-4">
          {approach_panel(s["approach"], full=True)}
        </div>'''
        if s.get("panels2"):
            extras += f'''
        <div class="row g-4 mt-1">
          <div class="col-lg-5">
          {info_panel(s["panels2"][0])}
          </div>
          <div class="col-lg-7">
          {info_panel(s["panels2"][1])}
          </div>
        </div>'''
        vp = value_strip(s["values"]) if s.get("values") else value_statement(s["value_text"])
        sec = sector_strip(s["sectors"]) if s.get("sectors") else ""
        out += f'''
    <!-- ================= SERVICE {n:02d}: {s["name"].upper()} ================= -->
    <section class="section service-section{soft}" id="{s["id"]}" aria-labelledby="{s["id"]}-title">
      <div class="container">
        <div class="row g-5 align-items-center mb-5">
          <div class="col-lg-6">
            <p class="eyebrow">Service {n:02d} / {len(SERVICES):02d}</p>
            <h2 class="section-title heading-accent" id="{s["id"]}-title">{s["title"]}</h2>
            <p class="tagline-spaced mb-4">{s["tagline"]}</p>
            <div class="lead-border">{intro}</div>
            <div class="mt-4">{quote_btn("Enquire about this service", service=s["name"])}</div>
          </div>
          <div class="col-lg-6">
            <div class="slant-frame">{media(s["img"], s["icon"], "4x3", "media-slant", s["name"])}</div>
            <p class="side-quote mt-4 mb-0">{s["quote"]}</p>
          </div>
        </div>

        <div class="d-flex flex-wrap align-items-end justify-content-between gap-2 mb-4">
          <h3 class="sub-title heading-accent mb-0">{s["cap_title"]}</h3>
          <p class="tagline-spaced small mb-0">{s["cap_sub"]}</p>
        </div>
        <div class="row row-cols-1 row-cols-md-2 row-cols-xl-3 g-4">
{caps}
        </div>{extras}{vp}{sec}

        <a class="back-link" href="#all-services">{i("bi-arrow-up")} Back to all services</a>
      </div>
    </section>
'''
    out += workflow_section()
    return out

def clients_main():
    groups = "\n".join(f'''          <div class="col"><div class="org-group"><div class="org-group-head">{i(ic)}{t}</div>
            <ul class="org-chips">{"".join(f'<li class="org-chip">{n}</li>' for n in names)}</ul></div></div>''' for ic, t, names in ORG_GROUPS)
    gov = "\n".join(f'''          <div class="col"><div class="gov-tile"><span class="gov-abbr">{a}</span><span class="gov-name">{n}</span></div></div>''' for a, n in GOV)
    exp = "\n".join(f'''          <div class="col"><div class="vp-item"><span class="icon-outline">{i(ic)}</span>
            <div><p class="vp-title">{t}</p><p class="vp-text">{txt}</p></div></div></div>''' for ic, t, txt in STRENGTH_EXP)
    sectors = "\n".join(f'''          <a class="sector" href="~P~services.html#{a}"><span class="sector-circle">{i(ic)}</span><span class="sector-label">{t}</span></a>''' for a, ic, t in SECTORS)
    return (banner("banner-clients.jpg", "Clients", "Trusted by leading organizations · Experienced across sectors", 'Clientele &amp; <span>Experience</span>',
                   "Experience that builds confidence for a stronger tomorrow.") + f'''
    <!-- CONFIRM before publishing: per the company profile (slide 13), these organizations are associated with the
         LEADERSHIP TEAM, and "specific team members, contracts and project references must be confirmed before
         publication". Names are shown as text; add logos only with permission from each organization. -->

    <!-- ================= INTRO ================= -->
    <section class="section pb-0" aria-labelledby="clients-intro-title">
      <div class="container">
        <div class="row g-5 align-items-center">
          <div class="col-lg-7">
            <p class="eyebrow">Our track record</p>
            <h2 class="section-title heading-accent" id="clients-intro-title">Clientele &amp; <span>Project Experience</span></h2>
            <div class="lead-border">
              <p>KALAGNI is promoted and led by a core team of experienced engineering professionals with a strong track record in the execution and delivery of electrical, infrastructure and industrial projects.</p>
              <p>The leadership team has been associated with, and has delivered services for, reputed national and multinational organizations across diverse sectors.</p>
            </div>
          </div>
          <div class="col-lg-5">
            <div class="slant-frame">{media("banner-clients.jpg", "bi-people", "4x3", "media-slant", "KALAGNI project experience")}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ================= ORGANIZATIONS BY SECTOR ================= -->
    <section class="section" aria-labelledby="orgs-title">
      <div class="container">
        {head("By sector", 'Organizations Associated with the <span>Leadership Team</span>', title_id="orgs-title")}
        <div class="row row-cols-1 row-cols-md-2 row-cols-xl-3 g-4">
{groups}
        </div>
      </div>
    </section>

    <!-- ================= GOVERNMENT ================= -->
    <section class="section section-soft" aria-labelledby="gov-title">
      <div class="container">
        {head("Public sector", 'Experience with <span>Government Organizations</span>', "The leadership team reports experience executing projects and services for government departments and public sector organizations across Telangana, Andhra Pradesh and Karnataka.", title_id="gov-title")}
        <div class="row row-cols-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-6 g-3">
{gov}
        </div>
      </div>
    </section>

    <!-- ================= STRENGTH THROUGH EXPERIENCE ================= -->
    <section class="section" aria-labelledby="strength-title">
      <div class="container">
        {head("What this means for you", 'Our Strength <span>Through Experience</span>', title_id="strength-title")}
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 g-4 mb-5">
{exp}
        </div>
        <div class="d-flex flex-wrap justify-content-center gap-4">
{sectors}
        </div>
      </div>
    </section>
''')

def contact_main():
    why = "\n".join(f'''              <div class="col"><div class="vp-item"><span class="icon-outline">{i(ic)}</span>
                <div><p class="vp-title">{t}</p><p class="vp-text">{txt}</p></div></div></div>''' for ic, t, txt in WHY_PARTNER)
    return (banner("banner-contact.jpg", "Contact", "Discuss | Partner | Plan | Execute | Grow", "Let's Build <span>Together</span>",
                   "Your projects. Our expertise. A stronger tomorrow.") + f'''
    <!-- ================= CONTACT DETAILS + FORM ================= -->
    <section class="section" id="contact-details" aria-labelledby="contact-title">
      <div class="container">
        <div class="row g-5">
          <div class="col-lg-5">
            <p class="eyebrow">Get in touch</p>
            <h2 class="section-title heading-accent" id="contact-title">Let's Build a <span>Stronger Tomorrow</span> Together</h2>
            <div class="lead-border mb-4">
              <p>KALAGNI is ready to partner with clients, consultants and institutions to deliver reliable, future-ready infrastructure across power, renewable energy, buildings and beyond.</p>
            </div>
            <div class="d-grid gap-3">
              <div class="contact-card"><span class="icon-ring icon-ring-sm">{i("bi-geo-alt-fill")}</span>
                <div><h3>Registered &amp; Corporate Office</h3><p>Plot No. 59, Lumbini Avenue, Gachibowli, Serilingampally, K.V. Rangareddy, Telangana 500032, India</p></div></div>
              <div class="contact-card"><span class="icon-ring icon-ring-sm">{i("bi-telephone-fill")}</span>
                <div><h3>Phone</h3><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div></div>
              <div class="contact-card"><span class="icon-ring icon-ring-sm">{i("bi-envelope-fill")}</span>
                <div><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
              <div class="contact-card"><span class="icon-ring icon-ring-sm">{i("bi-whatsapp")}</span>
                <div><h3>WhatsApp</h3><a href="{WHATSAPP}" target="_blank" rel="noopener">Chat with our team</a></div></div>
            </div>
          </div>
          <div class="col-lg-7">
            <div class="form-card">
              <h2 class="sub-title heading-accent mb-1">Send an <span>Enquiry</span></h2>
              <p class="text-body-secondary small mb-4">Fields marked <span class="req">*</span> are required.</p>
              {form_html("c")}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ================= LOCATION ================= -->
    <section class="section section-soft" aria-labelledby="location-title">
      <div class="container">
        {head("Our location", 'Strategically Located in <span>Hyderabad</span>', "Serving clients across Telangana, Andhra Pradesh and other regions in India.", title_id="location-title")}
        <!-- Google Maps embed: needs an internet connection -->
        <iframe class="map-frame" title="KALAGNI office location on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q=Lumbini+Avenue,+Gachibowli,+Hyderabad,+Telangana+500032&amp;output=embed"></iframe>
      </div>
    </section>

    <!-- ================= LEGAL & REGULATORY ================= -->
    <section class="section" aria-labelledby="legal-title">
      <div class="container">
        {head("Company information", 'Legal &amp; <span>Regulatory</span>', title_id="legal-title")}
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4 justify-content-center">
          <div class="col"><div class="legal-card">{i("bi-file-earmark-text")}<span class="legal-label">Company Name</span><span class="legal-value">KALAGNI Integrated Projects Private Limited</span></div></div>
          <div class="col"><div class="legal-card">{i("bi-building")}<span class="legal-label">CIN</span><span class="legal-value">U42202TS2026PTC224342</span></div></div>
          <div class="col"><div class="legal-card">{i("bi-receipt")}<span class="legal-label">GSTIN</span><span class="legal-value">36AANCK3239M1Z0</span></div></div>
          <!-- PAN card: add when the number is available (the profile says "To be inserted")
          <div class="col"><div class="legal-card"><i class="bi bi-person-vcard" aria-hidden="true"></i><span class="legal-label">PAN</span><span class="legal-value">XXXXXXXXXX</span></div></div> -->
        </div>

        <div class="value-strip mt-5">
          <div class="row g-4 align-items-center">
            <div class="col-xl-2">
              <p class="value-strip-label mb-0"><span class="icon-ring icon-ring-sm">{i("bi-people")}</span><span class="vsl-text">Why Partner <br class="d-none d-xl-inline"><span>with KALAGNI</span></span></p>
            </div>
            <div class="col-xl-10">
              <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-5 g-3">
{why}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
''' + certs_section())

PAGES = {
  "index.html": dict(R="", P="pages/", key="home", main=home_main, cta=True,
    TITLE="KALAGNI Integrated Projects | Integrated EPC Solutions",
    DESC="KALAGNI Integrated Projects Private Limited: integrated EPC solutions across power, solar and BESS, infrastructure, MEPF, HVAC, railway and digital engineering, from concept to commissioning."),
  "pages/about.html": dict(R="../", P="", key="about", main=about_main, cta=True,
    TITLE="About Us | KALAGNI Integrated Projects",
    DESC="Who we are, our values and the leadership team behind KALAGNI Integrated Projects Private Limited, Hyderabad."),
  "pages/services.html": dict(R="../", P="", key="services", main=services_main, cta=True,
    TITLE="Services | KALAGNI Integrated Projects",
    DESC="Electrical power infrastructure, solar and BESS, infrastructure and construction, MEPF, HVAC, railway and metro, engineering and digital solutions, approvals and O&M."),
  "pages/clients.html": dict(R="../", P="", key="clients", main=clients_main, cta=True,
    TITLE="Clients & Experience | KALAGNI Integrated Projects",
    DESC="Organizations and government bodies associated with the KALAGNI leadership team across power, infrastructure, industry and real estate."),
  "pages/contact.html": dict(R="../", P="", key="contact", main=contact_main, cta=False,
    TITLE="Contact Us | KALAGNI Integrated Projects",
    DESC="Contact KALAGNI Integrated Projects Private Limited, Plot No. 59, Lumbini Avenue, Gachibowli, Hyderabad, Telangana. Phone +91 9912485530."),
}

for path, cfg in PAGES.items():
    page = HEADER
    for k in ("home", "clients", "contact"):
        page = page.replace("{ACT_%s}" % k, ' active" aria-current="page' if k == cfg["key"] else "")
    for k in ("about", "services"):
        page = page.replace("{CLS_%s}" % k, " active" if k == cfg["key"] else "")
    for g in ("power", "build", "support"):
        page = page.replace("{ITEMS_%s}" % g, mega_items(g))
    page = page.replace("{TITLE}", esc(cfg["TITLE"])).replace("{DESC}", esc(cfg["DESC"]))
    page += cfg["main"]() + footer(cta=cfg["cta"])
    page = (page.replace("PHONE_TEL", PHONE_TEL).replace("PHONE_DISPLAY", PHONE_DISPLAY)
                .replace("WHATSAPP", WHATSAPP).replace("EMAIL", EMAIL)
                .replace("~R~", cfg["R"]).replace("~P~", cfg["P"]))
    (ROOT / path).write_text(page, encoding="utf-8")
    print(f"wrote {path:22s} {len(page):>7,} chars")
