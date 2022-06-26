from Execution_script import *
import streamlit as st
from streamlit_echarts import st_echarts
from PIL import Image

# LOADING IMAGES
im_sidebar = Image.open('/img_sidebar.png')
im_title = Image.open('/img_title.png')
# im_icon = Image.open('/icon.png')

# PAGE SET UP
st.set_page_config(
     page_title = 'Lead Score Analyzer',
     page_icon = 'icon.png',
     layout = 'wide',
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "### Lead score analyzer. \n\n The purpose of this data-driven application is to help the sales team of an online education company identify those potential customers most likely to buy the product. \n&nbsp; \n  \n To do this, a machine learning model based on a logistic regression algorithm is used, which takes as input data the information provided by the customer through a web form and that collected by the company's computer systems, and returns both a customer score and a recommendation as to whether it is profitable to manage the lead or not. \n&nbsp; \n  \n - Source code can be found [here](https://github.com/pedrocorma/lead-scoring-and-segmentation). \n - Further project details are available [here](https://pedrocorma.github.io/project/2leadscoring/)."
     })

# Page margins
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
                .css-hxt7ib{
                    padding-top: 2.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

# Sidebar width
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 485px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 300px;
        margin-left: -300px;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

# SIDEBAR
with st.sidebar:
    st.image(im_sidebar)
    st.markdown('')

    col1, col2, col3, col4, col5 = st.columns([0.5,1,0.25,1,0.5])
    with col2:
        form_button = st.button('NEW LEAD WEB FORM')
    with col4:
        calculate_button = st.button('CALCULATE SCORING')

    st.markdown('---')
    st.markdown("<h1 style='text-align: center; color: #f76497;'>SERVER-SIDE PARAMETERS</h1>", unsafe_allow_html=True)


    # Server-side features - Input
    col1,col2 = st.columns(2)
    with col1:
        lead_origin = st.selectbox('Lead origin', ['Landing Page Submission', 'API', 'Lead Add Form', 'Lead Import', 'Quick Add Form'], 0)
        last_activity = st.selectbox('Last activity',
                                     ['Email Opened','SMS Sent','Olark Chat Conversation','Page Visited on Website','Converted to Lead',
                                      'Email Link Clicked','Form Submitted on Website','Had a Phone Conversation','Approached upfront',
                                      'View in browser link Clicked','Visited Booth in Tradeshow','Email Received'],0)
        profile_score = st.slider('Profile score', 0, 20, value=16)
        total_visits = st.slider('Total visits', 0, 50, value=3)
    with col2:
        source = st.selectbox('Lead source',
                              ['Google','Direct Traffic','Olark Chat','Organic Search','Reference','Welingak Website','Referral Sites',
                               'Facebook','Null','Click2call','Press_Release','bing','Social Media','WeLearn','Pay per Click Ads',
                               'Live Chat','welearnblog_Home','youtubechannel','testone','blog','NC_EDM'],0)
        last_notable_activity = st.selectbox('Last notable activity',
                                             ['Modified','Email Opened','SMS Sent','Page Visited on Website','Email Link Clicked',
                                              'Olark Chat Conversation','Had a Phone Conversation','Email Marked Spam','Approached upfront',
                                              'Resubscribed to emails','View in browser link Clicked','Form Submitted on Website',
                                              'Email Received'],0)
        activity_score = st.slider('Activity score', 0, 20, value=14)
        page_views_per_visit = st.slider('Page views per visit', 0, 25, value=2)

    total_time_website = st.slider('Total time website (min)', 0, 60, value=8)



# MAIN
# Title image
col1,col2,col3 = st.columns([0.8,1,0.5])
with col2:
    st.image(im_title)

placeholder = st.empty()

with placeholder.container():
    st.markdown('')
    # Subtitle
    st.markdown("<h3 style='text-align: left; color: #f76497;'>LEAD WEB FORM</h3>", unsafe_allow_html=True)

    # Lead web form features - Input
    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox('Country', ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'],102)
        ocupation = st.selectbox('What is your current occupation?',
                                     ['Unemployed','Working Professional','Student','Other','Businessman','Housewife'],0)
        hear_about = st.selectbox('How did you hear about our company?',
                                      ['Select','Online Search','Word Of Mouth','Student of SomeSchool','Multiple Sources','Other','Advertisements',
                                       'Social Media','Email','SMS'],0)
        st.markdown(' ')

    with col2:
        city = st.selectbox('City',
                                ['Select','Mumbai','Thane & Outskirts','Other Cities','Other Cities of Maharashtra','Other Metro Cities',
                                 'Tier II Cities'],0)

        specialization = st.selectbox('Specialization',
                                          ['Select','Finance Management','Human Resource Management','Marketing Management',
                                           'Operations Management','Business Administration','IT Projects Management',
                                           'Banking, Investment And Insurance','Supply Chain Management','Media and Advertising',
                                           'Travel and Tourism','International Business','Healthcare Management','E-COMMERCE',
                                           'Hospitality Management','Retail Management','Rural and Agribusiness','E-Business',
                                           'Services Excellence'],0)
        matters_most = st.selectbox('What matters most to you in choosing this course?',
                                       ['Better Career Prospects','Unknown','Flexibility & Convenience','Other'],0)

    st.markdown('---')
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('Would you like to recieve more information about the course?')
    with col2:
        st.markdown("Are you interested in downloading a free copy of our book?")

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    col1,col2,col3 = st.columns([0.5,1,1.5])
    with col1:
        do_not_call = st.radio('Phone call',['Yes','No'],1)

    with col2:
        do_not_email = st.radio('Email',['Yes','No'],1)

    with col3:
        lead_magnet = st.radio('Interested',['Yes', 'No'],1)
    st.markdown('')


df_lead = pd.DataFrame({'activity_score':activity_score,
                        'city':city,
                        'country':country,
                        'do_not_call':do_not_call,
                        'do_not_email':do_not_email,
                        'hear_about':hear_about,
                        'last_activity':last_activity,
                        'last_notable_activity':last_notable_activity,
                        'lead_magnet':lead_magnet,
                        'lead_origin':lead_origin,
                        'matters_most':matters_most,
                        'ocupation':ocupation,
                        'page_views_per_visit':page_views_per_visit,
                        'profile_score':profile_score,
                        'source':source,
                        'specialization':specialization,
                        'total_time_website':total_time_website,
                        'total_visits':total_visits},index=[0])


# CALCULATE LEAD SCORING:
if calculate_button:
    scoring = run_model(df_lead)
    lead_score = int(scoring.lead_score[0]*100)
    manage_lead = scoring.manage_lead[0]
    placeholder.empty()
    placeholder_results = st.empty()

    def formatter_function(val):
        if val == 0.875*100:
            return('A')
        elif val == 0.625*100:
            return('B')
        elif val == 0.375*100:
            return('C')
        elif val == 0.125*100:
            return('D')
        return('')

    with placeholder_results.container():
        chart_options = {
        "stateAnimation": {"duration":300,
                           "easing":"cubicOut"},
        "animation": "true",
        "animationThreshold":2000,
        "animationDuration": 1000,
        "animationEasing": "cubicInOut",
        "animationDelay": 500,
        "animationDurationUpdate": 1000,
        "animationEasingUpdate": "cubicInOut",
        "animationDelayUpdate": 500,

        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [{"type": 'gauge',
                    "id": "ls",
                     "startAngle": 200,
                     "endAngle": -20,
                     "min": 0,
                     "max": 100,
                     "splitNumber": 10,
                    "animationThreshold": 2000,
                    "animationDuration": 1000,
                    "animationDurationUpdate": 1000,
                    "animationDelayUpdate": 500,
                    "animationEasing": 'cubicInOut',

                     "axisLine": {"lineStyle": {"width": 5,
                                                "color": [[0.25, '#FF6E76'],
                                                          [0.5, '#FDDD60'],
                                                          [0.75, '#58D9F9'],
                                                          [1, '#7CFFB2']]}},
                     "pointer": {"icon": 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
                                 "length": '15%',
                                 "width": 20,
                                 "offsetCenter": [0, '-65%'],
                                 "itemStyle": {"color": 'auto'}},
                      "axisTick": {"length": 10,
                                   "lineStyle": {"color": 'auto',
                                                 "width": 1}},
                      "splitLine": {"length": 15,
                                    "lineStyle": {"color": 'auto',
                                                  "width": 3}},
                      "axisLabel": {"color": '#464646',
                                    "fontSize": 25,
                                    "distance": -70,
                                    "formatter": formatter_function("{value}")},
                      "title": {"offsetCenter": [0, '-40%'],
                                "fontSize": 25},
                      "detail": {"valueAnimation": "true",
                                 "fontSize": 80,
                                 "offsetCenter": [0, '0%'],
                                 "formatter": "{value}",
                                 "color": 'auto'},
                      "data": [{"value": lead_score,
                                "name": 'Score'}]}],
                      "progress": {"show": "true", "width": 1,}
                                };
        st.markdown('---')
        col1,col2 = st.columns([1,0.8])
        if manage_lead=='Yes':
            with col1:
                st.markdown("<h4 style='text-align: center; color: #7CFFB2;'>It is cost-effective to manage this lead.</h4>", unsafe_allow_html=True)
            with col2:
                if lead_score >= 75:
                    st.markdown("<h4 style='text-align: center; color: #7CFFB2;'>Priority: Very high. </h4>", unsafe_allow_html=True)
                elif 50 <= lead_score < 75:
                    st.markdown("<h4 style='text-align: center; color: #58D9F9;'>Priority: High. </h4>", unsafe_allow_html=True)
                elif 25 <= lead_score < 50:
                    st.markdown("<h4 style='text-align: center; color: #FDDD60;'>Priority: Medium. </h4>", unsafe_allow_html=True)
                elif 25 > lead_score:
                    st.markdown("<h4 style='text-align: center; color: #FF6E76;'>Priority: Low. </h4>", unsafe_allow_html=True)
        elif manage_lead=='No':
            with col1:
                st.markdown("<h4 style='text-align: center; color: #FF6E76;'>It is not cost-effective to manage this lead.</h4>", unsafe_allow_html=True)
        st.markdown('---')
        results_plot = st_echarts(options=chart_options, width="100%", key=0, height='550%')



















##
