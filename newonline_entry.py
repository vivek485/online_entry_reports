import streamlit as st

from streamlit_option_menu import option_menu
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from deta import Deta


geptrlt = ['YEAR','BLOCK','REPORT FOR MONTH OF :-','Name of AHC :-','NEW PATIENTS','OLD PATIENTS','TOTAL PATIENTS','MALE PATIENTS','FEMALE PATIENTS','TOTAL PATIENTS.1','NADI','PAACHAN','RAKT','SWASHAN','MUTRA','TWAK','EAR/EYE','JWAR','OTHER','TOTAL']
ptrlt = ['YEAR','BLOCK','REPORT FOR MONTH OF :-','Name of AHC :-','NEW PATIENTS','OLD PATIENTS','TOTAL PATIENTS','MALE PATIENTS','FEMALE PATIENTS','CHILD PATIENTS','TOTAL PATIENTS.1','NADI','PAACHAN','RAKT','SWASHAN','MUTRA','TWAK','EAR/EYE','JWAR','OTHER','TOTAL']
adharcol=['YEAR',	'BLOCK','MONTH',	'NAME OF AHC',	'Total No. of patients attended',	'Total No. of MALE patients attended',	'Total No. of FEMALE patients attended',	'Total No. of Aadhar seeded beneficiaries',	'Total No. of beneficiaries having Mob. No.',	'DATE OF SESSION',	'TOTAL NO OF SESSION',	'NO OF MALE BENEFICIARY',	'NO OF FEMALE BENEFICIARY',	'NO OF CHILD BENEFICIARY',	'TOTAL NO OF YOGA BENEFICIARY IN MONTH']
bmwcol=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'YELLOW CATEGORY IN GRMS',	'RED CATEGORY IN GRMS',	'WHITE CATEGORY IN GRMS',	'BLUE CATEGORY IN GRMS',	'TOTAL IN GRMS',	'LIQUID WASTE GENERATED']
sapcol=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'DATE OF ACTIVITY',	'NAME OF SCHOOL',	'TYPE OF SCHOOL',	'SUBJECT COVERED',	'TOTAL BENEFICIARIES']
tbcol=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'Total monthly OPD (A)',	'New 70% Adult OPD (B)=out of A',	'No. of TB suspects for sputum microscopy (C)=out of B',	'Referral rate (D)=C/B x 100',	'TB suspects found positive (E)=out of C',	'Name of DMCs where patient was sent for sputum test (F)',	'Total TB patients on DOTS in AHC during the reporting month (A)',	'Total patients in Intensive Phase (B)=out of A',	'No. of patients in Continuation Phase (C)=out of A',	'No. Of TB patients died during the reporting month (D)=out of A',	'No of patients defaulted during the reporting month (E)=out of A',	'No. Of Sputum cups available on 1st day of reporting month (A)',	'No. Of Sputum cups available on last day of reporting month (B)',	'Total sputum cups required for next 1 month (C)',	'No. Of Referral slips available on 1st day of reporting month (D)',	'no of Referral slip available on last day of reporting month (E)',	'Total Referral slips required for next 1 month (F)']
pkcol=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'OPD_NEW',	'OPD_OLD',	'OPD_MALE',	'OPD_FEMALE',	'OPD_CHILD',	'OPD_TOTAL',	'IPD_NEW',	'IPD_OLD',	'IPD_MALE',	'IPD_FEMALE',	'IPD_CHILD',	'IPD_TOTAL']
kscol=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'NEW_OPD',	'OLD_OPD',	'MALE_OPD',	'FEMALE_OPD',	'CHILD_OPD',	'TOTAL_OPD',	'NEW_IPD',	'OLD_IPD',	'MALE_IPD',	'FEMALE_IPD',	'CHILD_IPD',	'TOTAL_IPD']
poshancol=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'MALE',	'FEMALE',	'CHILD',	'TOTAL']
ayuhimcol=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'AYUSHMAN_MALE',	'AYUSHMAN_FEMALE',	'AYUSHMAN_CHILD',	'AYUSHMAN_TOTAL',	'HIMCARE_MALE',	'HIMCARE_FEMALE',	'HIMCARE_CHILD',	'HIMCARE_TOTAL']
anucol=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'MARM',	'JALOKA',	'RAKTMOKSHAN',	'ALABU',	'MRITIKA',	'CUPPING',	'AGNIKARMA',	'KSHARKARMA']

KEY =st.secrets.db_key_credentials.mykey
deta = Deta(KEY)
def dbfunc(d,data,year,ahc,month):
    global db
    global deta
    #deta=
    db = deta.Base(d)
    us = str(year) + "_" + str(ahc) + '_'+str(month)
    db.put(data,key = us)
def get_pt(d):
    global db
    global deta
    global df
    #deta = 
    db = deta.Base(d)

    db_content = db.fetch().items
    if d =='reports':
        df = pd.DataFrame(db_content,columns=ptrlt)
        return df
    if d =='ger_reports':
        df = pd.DataFrame(db_content,columns=geptrlt)
        return df
    if d =='adahar_reports':
        df = pd.DataFrame(db_content,columns=adharcol)
        return df  
    if d =='bmw_reports':
        df = pd.DataFrame(db_content,columns=bmwcol)
        return df 
    if d =='sap_reports':
        df = pd.DataFrame(db_content,columns=sapcol)
        return df
    if d =='tb_reports':
        df = pd.DataFrame(db_content,columns=tbcol)
        return df
    if d =='pk_reports':
        df = pd.DataFrame(db_content,columns=pkcol)
        return df 
    if d =='ks_reports':
        df = pd.DataFrame(db_content,columns=kscol)
        return df
    if d =='poshan_reports':
        df = pd.DataFrame(db_content,columns=poshancol)
        return df
    if d =='ayuhim_reports':
        df = pd.DataFrame(db_content,columns=ayuhimcol)
        return df 
    if d =='anu_reports':
        df = pd.DataFrame(db_content,columns=anucol)
        return df    


st. set_page_config(layout="wide")
st.title("Reporting of District Shimla")


#-----------------------------------------------------------------------------

year_list = ['2024','2025','2026','2027']
block_list = ['SANDHU','SHIMLA','NERWA','RAMPUR','ROHRU']
Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
name_ahc_shimla = ['GALOT','ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
name_ahc_nerwa =['BAMTA',	'BHALOO',	'BHARAN',	'BHARANU',	'C/BAG',	'CHOPAL',	'DHAR CHANDNA',	'HALAU',	'JORNA',	'KHAGNA',	'KHAKHARONA',	'KIARNOO',	'MALTH',	'MAROG',	'NANHAR',	'NERWA',	'PORIYA',	'PULBAHAL',	'SHAMTHA',	'SHILA BAWAT',	'TAILOR',	'TANDAI',	'TIKKAR']
name_ahc_sandhu =['ALAWANG',	'BADEON',	'BAGHAL',	'BAGHI',	'BAGRI',	'CHEOG',	'DARKOTI',	'DHARONK',	'KAMAH',	'KHANETI',	'KIAR',	'KIARTOO',	'KUTHAR',	'MAHASU',	'NAGAN',	'PADGAYA',	'PANJANA',	'PURAG',	'RAWLAKIAR',	'SANDHU',	'SAROG',	'SATOG',	'SATANDRI',	'TIYALI']
name_ahc_rampur = ['AY.HOSP.RAMPUR','BATHARA',	'BHAMNOLI',	'BHAROG',	'DAGYANA',	'DANSA',	'DARAN',	'DARKALI',	'DELATH',	'DOFDA',	'DUTT NAGAR',	'GAHAN',	'GALANI',	'JAGORI',	'JAROL',	'JAWALDA',	'JUNI',	'KALEDA',	'KANDA',	'KANGAL',	'KANHAR',	'KASHAPAT',	'KATHINE',	'KHAMADI',	'KINNU',	'KKASHAPAT',	'KOOT',	'KUHAL',	'KUNGAL BALTI',	'LABANA',	'LOUGA',	'MAHOLI',	'MUNISH',	'NARAIN',	'NOGLI',	'PHANCHA',	'REOG',	'SANARSA',	'SARPARA',	'SHOLI',	'SURAD',	'THARU']
name_ahc_rohru =['ARHAL',	'AY.HOSP.ROHRU',	'BARARA',	'BASHTARI',	'DHAKRANTU',	'DHAR',	'GAJYANI',	'GHASNI',	'HARWANI',	'JAGTHAN',	'JAKHAR',	'JAKHNOTI',	'JANGLIK',	'JHARAG',	'K/PATHER',	'KADIWAN',	'KHARLA',	'KHAROT',	'KUDDU',	'KUI',	'LAROT',	'MASTOT',	'PANDRANU',	'PRAUNTHI',	'ROHAL',	'S/NAGAR',	'SALNA',	'SARIBASA',	'SAROT',	'SHEELGHAT',	'TIKKARI',	'TURAN']

lt = name_ahc_shimla
blc = 'SHIMLA'


#-------------------------------------------------------------------------
name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR',
'BAMTA',	'BHALOO',	'BHARAN',	'BHARANU',	'C/BAG',	'CHOPAL',	'DHAR CHANDNA',	'HALAU',	'JORNA',	'KHAGNA',	'KHAKHARONA',	'KIARNOO',	'MALTH',	'MAROG',	'NANHAR',	'NERWA',	'PORIYA',	'PULBAHAL',	'SHAMTHA',	'SHILA BAWAT',	'TAILOR',	'TANDAI',	'TIKKAR',
'ALAWANG',	'BADEON',	'BAGHAL',	'BAGHI',	'BAGRI',	'CHEOG',	'DARKOTI',	'DHARONK',	'KAMAH',	'KHANETI',	'KIAR',	'KIARTOO',	'KUTHAR',	'MAHASU',	'NAGAN',	'PADGAYA',	'PANJANA',	'PURAG',	'RAWLAKIAR',	'SANDHU',	'SAROG',	'SATOG',	'SATANDRI',	'TIYALI',
'BATHARA',	'BHAMNOLI',	'BHAROG',	'DAGYANA',	'DANSA',	'DARAN',	'DARKALI',	'DELATH',	'DOFDA',	'DUTT NAGAR',	'GAHAN',	'GALANI',	'JAGORI',	'JAROL',	'JAWALDA',	'JUNI',	'KALEDA',	'KANDA',	'KANGAL',	'KANHAR',	'KASHAPAT',	'KATHINE',	'KHAMADI',	'KINNU',	'KKASHAPAT',	'KOOT',	'KUHAL',	'KUNGAL BALTI',	'LABANA',	'LOUGA',	'MAHOLI',	'MUNISH',	'NARAIN',	'NOGLI',	'PHANCHA',	'REOG',	'SANARSA',	'SARPARA',	'SHOLI',	'SURAD',	'THARU',
'ARHAL',	'AY.HOSP.ROHRU',	'BARARA',	'BASHTARI',	'DHAKRANTU',	'DHAR',	'GAJYANI',	'GHASNI',	'HARWANI',	'JAGTHAN',	'JAKHAR',	'JAKHNOTI',	'JANGLIK',	'JHARAG',	'K/PATHER',	'KADIWAN',	'KHARLA',	'KHAROT',	'KUDDU',	'KUI',	'LAROT',	'MASTOT',	'PANDRANU',	'PRAUNTHI',	'ROHAL',	'S/NAGAR',	'SALNA',	'SARIBASA',	'SAROT',	'SHEELGHAT',	'TIKKARI',	'TURAN']

#--------------------------------------------------------------------------
def select_block(a):
    global lt 
    global blc
    bloc = st.radio('Select Block for which you want to fill report',block_list,index=None,horizontal=True,key=a)
    if bloc == 'SHIMLA':
        lt = name_ahc_shimla
        blc = 'SHIMLA'
    elif bloc == 'SANDHU':
        lt = name_ahc_sandhu
        blc = 'SANDHU'
    elif bloc == 'NERWA':
        lt = name_ahc_nerwa
        blc = 'NERWA'
    elif bloc == 'RAMPUR':
        lt = name_ahc_rampur
        blc = 'RAMPUR'
    elif bloc == 'ROHRU':
        lt = name_ahc_rohru
        blc = 'ROHRU'




# op_list = ["Home", "Monthly PTR", "Geriatric PTR", 'Aadhar Seeded / Saptahic yog','BMW','SAP','TB Mukt','Ksharsutra','AnuShastra','Panchkarma_PTR','Poshan','AYUSHMAN_HIMCARE','Edit/View','Consolidated Reports']
# selected2 = st.radio('Select Option for which you want to fill report',op_list,index=None,horizontal=True)

selected2 = option_menu("AYUSH VIBHAG HIMACHAL PRADESH", ["Home", "Monthly PTR", "Geriatric PTR", 'Aadhar Seeded / Saptahic yog','BMW','SAP','TB Mukt','Ksharsutra','AnuShastra','Panchkarma_PTR','Poshan','AYUSHMAN_HIMCARE','Edit/View','Consolidated Reports'], 
icons=['house', 'boxes', "boxes", 'boxes','boxes','boxes','boxes','boxes','boxes','boxes','boxes','boxes'], 
menu_icon="cast", default_index=0, orientation="horizontal")

def edit_entry():
    with st.sidebar:       
#actions....................................................
        action = st.selectbox('Choose an action',['Edit Entry','View Entries'])
        if action == 'View Entries':
            st.markdown('Select AHC and report to view entries made...')
            ac1 = st.selectbox('Choose from below',options=["Monthly PTR", "Geriatric PTR", 'Aadhar Seeded','BMW','SAP','TB Mukt','Ksharsutra','Panchkarma_PTR','Poshan','AYUSHMAN_HIMCARE','AnuShastra'])
            
            if ac1 == 'Monthly PTR':
                select_block(a='a1')
                ahc = st.selectbox('select AHC',options=lt)
                get_pt(d='reports')
                st.write(df[df['Name of AHC :-'] == ahc])
                # df = df[df['Name of AHC :-']== st.selectbox('select AHC',options=name_ahc)]
                # st.write(df)
                

            elif ac1 == 'Geriatric PTR':
                select_block(a='a2')
                ahc = st.selectbox('select AHC',options=lt)
                get_pt(d='ger_reports')
                st.write(df[df['Name of AHC :-'] == ahc])
            elif ac1 == 'Aadhar Seeded':
                select_block(a='a3')
                ahc = st.selectbox('select AHC',options=lt)
                get_pt(d='adahar_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
            elif ac1 == 'BMW':
                select_block(a='a4')
                ahc = st.selectbox('select AHC',options=lt)
                get_pt(d='bmw_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
            elif ac1 == 'SAP':
                select_block(a='a5')
                ahc = st.selectbox('select AHC',options=lt)
                get_pt(d='sap_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
            elif ac1 == 'TB Mukt':
                select_block(a='a6')
                ahc = st.selectbox('select AHC',options=lt)
                get_pt(d='tb_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
            elif ac1 == 'Panchkarma_PTR':
                hosp = ['AYU HOSPITAL ROHRU','AYU HOSPITAL RAMPUR']
                
                ahc = st.selectbox('select Hospital',options=hosp)
                get_pt(d='pk_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
            elif ac1 == 'Ksharsutra':
                hosp = ['AYU HOSPITAL ROHRU','AYU HOSPITAL RAMPUR']
                
                ahc = st.selectbox('select Hospital',options=hosp)
                get_pt(d='ks_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
               
            elif ac1 == 'Poshan':
                select_block(a='a7')
                ahc = st.selectbox('select AHC',options=lt)
                get_pt(d='poshan_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
            elif ac1 == 'AYUSHMAN_HIMCARE':
                hosp = ['AYU HOSPITAL ROHRU','AYU HOSPITAL RAMPUR']
                
                ahc = st.selectbox('select Hospital',options=hosp)
                get_pt(d='ayuhim_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
            elif ac1 == 'AnuShastra':
                select_block(a='a8')
                ahc = st.selectbox('select AHC',options=lt)
                get_pt(d='anu_reports')
                st.write(df[df['NAME OF AHC'] == ahc])
#edit---------------------------------------------------------------------------------------------------------------------------------------   
        
        if action == 'Edit Entry':
            st.write('## Make entry from main window your previous entry will be updated ##')

          
if selected2 == 'Edit/View':
    edit_entry()
#selected2

def home():
    #st.title('Reporting of District Shimla')
    st.markdown('click on above tabs to submit new reports....')
    st.divider()

    b = st.button('Click to view Total PTR Reports till today')

    if b:
        get_pt(d='reports')
        df2=pd.DataFrame(df)
        l=ptrlt[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','REPORT FOR MONTH OF :-'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)


    c = st.button('Click to view Total Geriatric PTR Reports till today')
    if c:

        get_pt(d='ger_reports')
        df2=pd.DataFrame(df)
        l=geptrlt[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','REPORT FOR MONTH OF :-'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    d = st.button('Click to view Total Adhar/Yog Reports till today')
    if d:
        get_pt(d='adahar_reports')
        df2=pd.DataFrame(df)
        adharcol1=['YEAR',	'BLOCK','MONTH',	'NAME OF AHC',	'Total No. of patients attended',	'Total No. of MALE patients attended',	'Total No. of FEMALE patients attended',	'Total No. of Aadhar seeded beneficiaries',	'Total No. of beneficiaries having Mob. No.','TOTAL NO OF SESSION',	'NO OF MALE BENEFICIARY',	'NO OF FEMALE BENEFICIARY',	'NO OF CHILD BENEFICIARY',	'TOTAL NO OF YOGA BENEFICIARY IN MONTH']
        l=adharcol1[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    e = st.button('Click to view Total BMW Reports till today')
    if e:
        get_pt(d='bmw_reports')
        df2=pd.DataFrame(df)
        l=bmwcol[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    f = st.button('Click to view Total SAP Reports till today')
    if f:
        get_pt(d='sap_reports')
        df2=pd.DataFrame(df)
        l=sapcol[-1:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    j = st.button('Click to view Total TB Mukt Reports till today')
    if j:
        get_pt(d='tb_reports')
        df2=pd.DataFrame(df)
        tbcol1=['YEAR',	'BLOCK',	'MONTH',	'NAME OF AHC',	'Total monthly OPD (A)',	'New 70% Adult OPD (B)=out of A',	'No. of TB suspects for sputum microscopy (C)=out of B',	'Referral rate (D)=C/B x 100',	'TB suspects found positive (E)=out of C',	'Total TB patients on DOTS in AHC during the reporting month (A)',	'Total patients in Intensive Phase (B)=out of A',	'No. of patients in Continuation Phase (C)=out of A',	'No. Of TB patients died during the reporting month (D)=out of A',	'No of patients defaulted during the reporting month (E)=out of A',	'No. Of Sputum cups available on 1st day of reporting month (A)',	'No. Of Sputum cups available on last day of reporting month (B)',	'Total sputum cups required for next 1 month (C)',	'No. Of Referral slips available on 1st day of reporting month (D)',	'no of Referral slip available on last day of reporting month (E)',	'Total Referral slips required for next 1 month (F)']
        l=tbcol1[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    g = st.button('Click to view Total Panchkarma Reports till today')
    if g:
        get_pt(d='pk_reports')
        df2=pd.DataFrame(df)
        l=pkcol[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    p = st.button('Click to view Total Ksharsutra Reports till today')
    if p:
        get_pt(d='ks_reports')
        df2=pd.DataFrame(df)
        l=kscol[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    h = st.button('Click to view Total Poshan Reports till today')
    if h:
        get_pt(d='poshan_reports')
        df2=pd.DataFrame(df)
        l=poshancol[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    i = st.button('Click to view Total Ayushman/Himcare Reports till today')
    if i:
        get_pt(d='ayuhim_reports')
        df2=pd.DataFrame(df)
        l=ayuhimcol[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    m = st.button('Click to view Total Anushastra Reports till today')
    if m:
        get_pt(d='anu_reports')
        df2=pd.DataFrame(df)
        l=anucol[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df3=df2.groupby(['BLOCK','MONTH'])[l].sum()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    v = st.button('Click to view >300 report till today')
    if v:
        get_pt(d='reports')
        df2=pd.DataFrame(df)
        l1= ['YEAR','BLOCK','REPORT FOR MONTH OF :-','Name of AHC :-','NEW PATIENTS','OLD PATIENTS','MALE PATIENTS','FEMALE PATIENTS','CHILD PATIENTS','TOTAL']
        l= l1[4:]
        df2[l]=df2[l].apply(pd.to_numeric,errors='coerce', axis=1)
        df2=df2[df2['NEW PATIENTS']>=300]
        
        df3=df2.groupby(['BLOCK','REPORT FOR MONTH OF :-'])[l].sum()
        df6=df2.groupby(['BLOCK','REPORT FOR MONTH OF :-','Name of AHC :-'])['Name of AHC :-'].count()
        df4=df2.groupby(['BLOCK'])[l].sum()
        df5=df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
        st.write('## Total AHC with opd>300 of District Shimla Blockwise ##')
        st.dataframe(df6)

        
if selected2 == 'Home' :
    home()

    


def ptr():
    
    
    st.title('Patients Treated Reports')
    st.markdown('Enter All Details Below')
    

    select_block(a='a1')
    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='PTR'):
        year = st.selectbox("Year*",options=year_list)
        block = blc #st.selectbox('Block',options=block_list)
        #date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*",options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=lt)
        nw = st.text_input(label="New*")
        ol =st.text_input(label="Old*")
        t = st.text_input(label="Total*")
        m = st.text_input(label="Male*")
        f = st.text_input(label="Female*")
        ch = st.text_input(label="Child*")
        ts=st.text_input(label="Total_*")
        nad = st.text_input(label="Nadi*")
        pac = st.text_input(label="Pachan*")
        rak = st.text_input(label="Rakt*")
        shw = st.text_input(label="Shwashan*")
        mut = st.text_input(label="Mutra*")
        tw = st.text_input(label="Tvak*")
        er = st.text_input(label="Eye/Ear*")
        jw = st.text_input(label="Jwar*")
        ot = st.text_input(label="Other*")
        td =  st.text_input(label="Total.*")
        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit PTR Report')
    
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block or not ahc or not nw or not ol or not t or not m or not f or not ch or not ts or not nad or not pac or not rak or not shw or not mut or not tw or not er or not jw or not ot or not td :
                st.warning('Ensure all fields are filled')




        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,
                    'REPORT FOR MONTH OF :-':month,
                    'Name of AHC :-':ahc,
                    'NEW PATIENTS':nw,
                    'OLD PATIENTS':ol,
                    'TOTAL PATIENTS':t,
                    'MALE PATIENTS':m,
                    'FEMALE PATIENTS':f,
                    'CHILD PATIENTS':ch,
                    'TOTAL PATIENTS.1':ts,
                    'NADI':nad,
                    'PAACHAN':pac,
                    'RAKT':rak,
                    'SWASHAN':shw,
                    'MUTRA':mut,
                    'TWAK':tw,
                    'EAR/EYE':er,
                    'JWAR':jw,
                    'OTHER':ot,
                    'TOTAL':td}


                if ptr_data['NEW PATIENTS'] != ptr_data['TOTAL']:
                    st.warning("Kindly check New Patients are not matching with total of Nadi Paachan...............")
                    st.stop()
                    
                elif int(ptr_data['NEW PATIENTS']) + int(ptr_data['OLD PATIENTS']) != int(ptr_data['TOTAL PATIENTS']):
                    st.warning("Kindly check Sum of New Patients and Old Patients  is not matching with Total...............")
                    st.stop()
                elif int(ptr_data['MALE PATIENTS']) + int(ptr_data['FEMALE PATIENTS'])+ int(ptr_data['CHILD PATIENTS']) != int(ptr_data['TOTAL PATIENTS.1']):
                    st.warning("Kindly check Sum of Male ,Female and Child is not matching with Total...............")
                    st.stop()

                
                

                data = ptr_data
                   
                    
                dbfunc(d='reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))


if selected2 == 'Monthly PTR':
    ptr()


def geriatric():

    
    
    st.title('Geriatric Patients Treated Reports')
    st.markdown('Enter All Details Below')


    #st.dataframe(existingdata_gr)
    select_block(a='b1')
    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='Geriatric_PTR'):
        year = st.selectbox("Year*",options=year_list)
        block = blc#st.selectbox('Block',options=block_list)
        #date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*",options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=lt)
        nw = st.text_input(label="New*")
        ol =st.text_input(label="Old*")
        #t = st.text_input(label="Total*")
        m = st.text_input(label="Male*")
        f = st.text_input(label="Female*")
        #ch = st.text_input(label="Child*")
        #ts= st.text_input(label="Total_*")
        nad = st.text_input(label="Nadi*")
        pac = st.text_input(label="Pachan*")
        rak = st.text_input(label="Rakt*")
        shw = st.text_input(label="Shwashan*")
        mut = st.text_input(label="Mutra*")
        tw = st.text_input(label="Tvak*")
        er = st.text_input(label="Eye/Ear*")
        jw = st.text_input(label="Jwar*")
        ot = st.text_input(label="Other*")
        #td = st.text_input(label="Total.*")
        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Geriatric PTR Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block or not ahc or not nw or not ol  or not m or not f   or not nad or not pac or not rak or not shw or not mut or not tw or not er or not jw or not ot  :
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,                   
                    
                    'REPORT FOR MONTH OF :-':month,
                    'Name of AHC :-':ahc,
                    'NEW PATIENTS':nw,
                    'OLD PATIENTS':ol,
                    'TOTAL PATIENTS':int(nw) + int(ol),
                    'MALE PATIENTS':m,
                    'FEMALE PATIENTS':f,
                    'TOTAL PATIENTS.1':int(m)+ int(f),
                    'NADI':nad,
                    'PAACHAN':pac,
                    'RAKT':rak,
                    'SWASHAN':shw,
                    'MUTRA':mut,
                    'TWAK':tw,
                    'EAR/EYE':er,
                    'JWAR':jw,
                    'OTHER':ot,
                    'TOTAL':int(nad)+int(pac)+int(rak)+int(shw)+int(mut)+int(tw)+int(er)+int(jw)+int(ot)}
                
                # if ptr_data['NEW PATIENTS'] != ptr_data['TOTAL']:
                #     st.warning("Kindly check New Patients are not matching with total of Nadi Paachan...............")
                #     st.stop()
                    
                # elif int(ptr_data['NEW PATIENTS']) + int(ptr_data['OLD PATIENTS']) != int(ptr_data['TOTAL PATIENTS']):
                #     st.warning("Kindly check Sum of New Patients and Old Patients  is not matching with Total...............")
                #     st.stop()
                # elif int(ptr_data['MALE PATIENTS']) + int(ptr_data['FEMALE PATIENTS'])+ int(ptr_data['CHILD PATIENTS']) != int(ptr_data['TOTAL PATIENTS.1']):
                #     st.warning("Kindly check Sum of Male ,Female and Child is not matching with Total...............")
                #     st.stop()

                
                

                data = ptr_data
                   
                    
                dbfunc(d='ger_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))




if selected2 == "Geriatric PTR":
    geriatric()



def adhar():

    
    
    st.title('Aadhar Reports')
    st.markdown('Enter All Details Below')


    #st.dataframe(existingdata_ad)
    select_block(a='c1')
    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='Aadhar/yog'):
        year = st.selectbox("Year*",options=year_list)
        block = blc#st.selectbox('Block',options=block_list)
        #date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*",options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=lt)
        #nw_ = st.text_input(label="Total No. of patients attended*")
        ol_ =st.text_input(label="Total No. of MALE patients attended*")
        t_f =st.text_input(label="Total No. of FEMALE patients attended*")
        t_ = st.text_input(label="Total No. of Aadhar seeded beneficiaries*")
        m_ = st.text_input(label="Total No. of beneficiaries having Mob. No.*")
        f_ = st.text_input(label="DATE OF SESSION*")
        ch_ = st.text_input(label="TOTAL NO OF SESSION*")
        ts_ =st.text_input(label="NO OF MALE BENEFICIARY*")
        nad_ = st.text_input(label="NO OF FEMALE BENEFICIARY*")
        pac_ = st.text_input(label="NO OF CHILD BENEFICIARY*")
        #rak_ = st.text_input(label="TOTAL NO OF YOGA BENEFICIARY IN MONTH*")

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Adhar/Yog Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block or not ahc or not ol_ or not t_ or not t_f or not m_ or not f_  or not ts_ or not nad_ or not pac_  :
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,
            
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'Total No. of patients attended':int(ol_)+int(t_f),
                    'Total No. of MALE patients attended':ol_,
                    'Total No. of FEMALE patients attended':t_f,
                    'Total No. of Aadhar seeded beneficiaries':t_,
                    'Total No. of beneficiaries having Mob. No.':m_,
                    'DATE OF SESSION':f_,
                    'TOTAL NO OF SESSION':ch_,
                    'NO OF MALE BENEFICIARY':ts_,
                    'NO OF FEMALE BENEFICIARY':nad_,
                    'NO OF CHILD BENEFICIARY':pac_,
                    'TOTAL NO OF YOGA BENEFICIARY IN MONTH':int(ts_)+int(nad_)+int(pac_)}

                data = ptr_data
                   
                    
                dbfunc(d='adahar_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))


if selected2 == 'Aadhar Seeded / Saptahic yog':
    adhar()


def bmw():

    
    
    st.title('Bio Medical Waste Report')
    st.markdown('# Enter All Details Below donot write gms in front of value')

    # #st.dataframe(existingdata_ad)
    select_block(a='d1')
    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='BMW Report'):
        year = st.selectbox("Year*",options=year_list)
        block = blc#st.selectbox('Block',options=block_list)
        #date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*",options= Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=lt)
        yl = st.text_input(label="YELLOW CATEGORY IN GRMS*")
        rd =st.text_input(label="RED CATEGORY IN GRMS*")
        wh =st.text_input(label="WHITE CATEGORY IN GRMS*")
        bl = st.text_input(label="BLUE CATEGORY IN GRMS*")
        tl = st.text_input(label="TOTAL IN GRMS*")
        lq = st.text_input(label="LIQUID WASTE GENERATED in liters*")


        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit BMW Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block or not ahc  or not yl or not rd  or not wh or not bl  or not lq :
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data={
                    'YEAR':int(year),
                    'BLOCK':block,
                
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'YELLOW CATEGORY IN GRMS':yl,
                    'RED CATEGORY IN GRMS':rd,
                    'WHITE CATEGORY IN GRMS':wh,
                    'BLUE CATEGORY IN GRMS':bl,
                    'TOTAL IN GRMS':tl, #int(yl)+int(rd)+int(wh)+int(bl),
                    'LIQUID WASTE GENERATED':lq}
                data = ptr_data
                   
                    
                dbfunc(d='bmw_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))

if selected2 == 'BMW':
    bmw()


def sap():

    
    
    st.title('School Adoption Report')
    st.markdown('Enter All Details Below')


    select_block(a='e1')
    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    school_type =['Primary','Sr Secondary','Middle','College','Others']
    with st.form(key='SAP Report'):
        year = st.selectbox("Year*",options=year_list)
        block = blc#st.selectbox('Block',options=block_list)

        month = st.selectbox("Month*",options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=lt)
        yl = st.text_input(label="DATE OF ACTIVITY*")
        rd =st.text_input(label="NAME OF SCHOOL*")
        wh =st.selectbox("TYPE OF SCHOOL*",options = school_type)
        bl = st.text_input(label="SUBJECT COVERED*")
        tl = st.text_input(label="TOTAL BENEFICIARIES*")



        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit SAP Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block  or not ahc  or not yl or not rd  or not wh or not bl or not tl  :
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data={
                    'YEAR':int(year),
                    'BLOCK':block,
                    
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'DATE OF ACTIVITY':yl,
                    'NAME OF SCHOOL':rd,
                    'TYPE OF SCHOOL':wh,
                    'SUBJECT COVERED':bl,
                    'TOTAL BENEFICIARIES':tl}
                data = ptr_data
                   
                    
                dbfunc(d='sap_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))
#------------------------------------------------total school visited
if selected2 == 'SAP':
    sap()


def tbmukt():
    
    
    st.title('Patients TB Mukt Reports')
    st.markdown('Enter All Details Below')


     #st.dataframe(existingdata)
    select_block(a='f1')
    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='TB Mukt'):
        year = st.selectbox("Year*",options=year_list)
        block = blc#st.selectbox('Block',options=block_list)
      
        month = st.selectbox("Month*",options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=lt)
        nw = st.text_input(label="Total monthly OPD (A)*")
        ol =st.text_input(label="New 70% Adult OPD (B)=out of A*")
        t = st.text_input(label="No. of TB suspects for sputum microscopy (C)=out of B*")
        m = st.text_input(label="Referral rate (D)=C/B x 100*")
        f = st.text_input(label="TB suspects found positive (E)=out of C*")
        ch = st.text_input(label="Name of DMCs where patient was sent for sputum test (F)*")
        ts=st.text_input(label="Total TB patients on DOTS in AHC during the reporting month (A)*")
        nad = st.text_input(label="Total patients in Intensive Phase (B)=out of A*")
        pac = st.text_input(label="No. of patients in Continuation Phase (C)=out of A*")
        rak = st.text_input(label="No. Of TB patients died during the reporting month (D)=out of A*")
        shw = st.text_input(label="No of patients defaulted during the reporting month (E)=out of A*")
        mut = st.text_input(label="No. Of Sputum cups available on 1st day of reporting month (A)*")
        tw = st.text_input(label="No. Of Sputum cups available on last day of reporting month (B)*")
        er = st.text_input(label="Total sputum cups required for next 1 month (C)*")
        jw = st.text_input(label="No. Of Referral slips available on 1st day of reporting month (D)*")
        ot = st.text_input(label="no of Referral slip available on last day of reporting month (E)*")
        td = st.text_input(label="Total Referral slips required for next 1 month (F)*")
        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit TB Mukt Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block or not ahc or not nw or not ol or not t or not m or not f or not ch or not ts or not nad or not pac or not rak or not shw or not mut or not tw or not er or not jw or not ot or not td :
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,
                    
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'Total monthly OPD (A)':nw,
                    'New 70% Adult OPD (B)=out of A':ol,
                    'No. of TB suspects for sputum microscopy (C)=out of B':t,
                    'Referral rate (D)=C/B x 100':m,
                    'TB suspects found positive (E)=out of C':f,
                    'Name of DMCs where patient was sent for sputum test (F)':ch,
                    'Total TB patients on DOTS in AHC during the reporting month (A)':ts,
                    'Total patients in Intensive Phase (B)=out of A':nad,
                    'No. of patients in Continuation Phase (C)=out of A':pac,
                    'No. Of TB patients died during the reporting month (D)=out of A':rak,
                    'No of patients defaulted during the reporting month (E)=out of A':shw,
                    'No. Of Sputum cups available on 1st day of reporting month (A)':mut,
                    'No. Of Sputum cups available on last day of reporting month (B)':tw,
                    'Total sputum cups required for next 1 month (C)':er,
                    'No. Of Referral slips available on 1st day of reporting month (D)':jw,
                    'no of Referral slip available on last day of reporting month (E)':ot,
                    'Total Referral slips required for next 1 month (F)':td}
                data = ptr_data
                   
                    
                dbfunc(d='tb_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))


if selected2 == 'TB Mukt':
    tbmukt()


def panchkarma_ptr():
    st.title('Panchkarma Report IPD/OPD')
    st.markdown('Enter All Details Below')

   
    #st.dataframe(existingdata_ad)

    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    hosp = ['AYU HOSPITAL ROHRU','AYU HOSPITAL RAMPUR']
    block = ['SHIMLA']
    with st.form(key='Panchkarma Report'):
        year = st.selectbox("Year*",options=year_list)
        block = st.selectbox('Block',options=block)
      
        month = st.selectbox("Month*",options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=hosp)
        yl = st.text_input(label="OPD_NEW*")
        rd =st.text_input(label="OPD_OLD*")
        wh =st.text_input(label="OPD_MALE*")
        whf =st.text_input(label="OPD_FEMALE*")
        whc =st.text_input(label="OPD_CHILD*")
        bl = st.text_input(label="OPD_TOTAL*")
        yl1 = st.text_input(label="IPD_NEW*")
        rd1 =st.text_input(label="IPD_OLD*")
        wh1 =st.text_input(label="IPD_MALE*")
        whf1 =st.text_input(label="IPD_FEMALE*")
        whc1 =st.text_input(label="IPD_CHILD*")
        bl1 = st.text_input(label="IPD_TOTAL*")




        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Panchkarma Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block  or not ahc  or not yl or not rd  or not wh or not whf or not whc or not yl1 or not rd1 or not bl  or not rd1  or not whf1 or not whc1 or not bl1   :
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,
                    
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'OPD_NEW':yl,
                    'OPD_OLD':rd,
                    'OPD_MALE':wh,
                    'OPD_FEMALE':whf,
                    'OPD_CHILD':whc,
                    'OPD_TOTAL':bl,
                    'IPD_NEW':yl1,
                    'IPD_OLD':rd1,
                    'IPD_MALE':wh1,
                    'IPD_FEMALE':whf1,
                    'IPD_CHILD':whc1,
                    'IPD_TOTAL':bl1}
                data = ptr_data
                   
                    
                dbfunc(d='pk_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))



if selected2 == 'Panchkarma_PTR':
    panchkarma_ptr()


def poshan():
    
    
    
    st.title('Poshan Report')
    st.markdown('Enter All Details Below')
   
    #st.dataframe(existingdata_ad)
    select_block(a='g1')
    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']

    with st.form(key='Poshan Report'):
        year = st.selectbox("Year*",options=year_list)
        block = blc#st.selectbox('Block',options=block_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=lt)   
        #date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*",options=Month_list)
        yl = st.text_input(label="MALE*")
        rd =st.text_input(label="FEMALE*")
        bl = st.text_input(label="CHILD*")
        tl = st.text_input(label="TOTAL*")



        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Poshan Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block  or not ahc  or not yl or not rd  or not bl or not tl  :
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,
        
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'MALE':yl,
                    'FEMALE':rd,
                    'CHILD':bl,
                    'TOTAL':tl}
                data = ptr_data
                   
                    
                dbfunc(d='poshan_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))


if selected2 == 'Poshan':
    poshan()

def ayuhim():
    
    
    
    st.title('Ayushman Himcare Report')
    st.markdown('Enter All Details Below')

    #st.dataframe(existingdata_ad)

    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    hosp = ['AYU HOSPITAL ROHRU','AYU HOSPITAL RAMPUR']
    block = ['SHIMLA']
    # #st.dataframe(existingdata_ad)

    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='Ayushman Report'):
        year = st.selectbox("Year*",options=year_list)
        block = st.selectbox('Block',options=block)
        #date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*",options= Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=hosp)
        yl = st.text_input(label="AYUSHMAN_MALE*")
        rd =st.text_input(label="AYUSHMAN_FEMALE*")
        wh =st.text_input(label="AYUSHMAN_CHILD*")
        bl = st.text_input(label="AYUSHMAN_TOTAL*")
        tl = st.text_input(label="HIMCARE_MALE*")
        lq = st.text_input(label="HIMCARE_FEMALE*")
        lqc = st.text_input(label="HIMCARE_CHILD*")
        lq1 = st.text_input(label="HIMCARE_TOTAL*")


        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Ayushman/Himcare Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block or not ahc  or not yl or not rd  or not wh or not bl or not tl or not lq or not lqc or not lq1:
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,
                
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'AYUSHMAN_MALE':yl,
                    'AYUSHMAN_FEMALE':rd,
                    'AYUSHMAN_CHILD':wh,
                    'AYUSHMAN_TOTAL':bl,
                    'HIMCARE_MALE':tl,
                    'HIMCARE_FEMALE':lq,
                    'HIMCARE_CHILD':lqc,
                    'HIMCARE_TOTAL':lq1}
                data = ptr_data
                   
                    
                dbfunc(d='ayuhim_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))


if selected2 == 'AYUSHMAN_HIMCARE':
    ayuhim()

def kshar():
    
    
    
    st.title('Ksharsutra Report')
    st.markdown('Enter All Details Below')

    #st.dataframe(existingdata_ad)

    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    hosp = ['AYU HOSPITAL ROHRU','AYU HOSPITAL RAMPUR']
    block = ['SHIMLA']
    # #st.dataframe(existingdata_ad)

    #Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='Ksharsutra Report'):
        year = st.selectbox("Year*",options=year_list)
        block = st.selectbox('Block',options=block)
        #date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*",options= Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=hosp)
        nw =st.text_input(label='NEW_OPD*')
        ol =st.text_input(label='OLD_OPD*')
        yl = st.text_input(label="MALE_OPD*")
        rd =st.text_input(label="FEMALE_OPD*")
        wh =st.text_input(label="CHILD_OPD*")
        bl = st.text_input(label="TOTAL_OPD*")
        nw1 =st.text_input(label='NEW_IPD*')
        ol1 =st.text_input(label='OLD_IPD*')
        tl = st.text_input(label="MALE_IPD*")
        lq = st.text_input(label="FEMALE_IPD*")
        lqc = st.text_input(label="CHILD_IPD*")
        lq1 = st.text_input(label="TOTAL_IPD*")


        st.markdown('**required*')
        submit_button = st.form_submit_button(label='SUBMIT KSHARSUTRA Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block or not ahc  or not yl or not rd  or not wh or not bl or not tl or not lq or not lqc or not lq1 or not nw or not nw1 or not ol or not ol1:
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,
                    
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'NEW_OPD':nw,
                    'OLD_OPD':ol,
                    'MALE_OPD':yl,
                    'FEMALE_OPD':rd,
                    'CHILD_OPD':wh,
                    'TOTAL_OPD':bl,
                    'NEW_IPD':nw1,
                    'OLD_IPD':ol1,
                    'MALE_IPD':tl,
                    'FEMALE_IPD':lq,
                    'CHILD_IPD':lqc,
                    'TOTAL_IPD':lq1}
                data = ptr_data
                   
                    
                dbfunc(d='ks_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))

if selected2 == 'Ksharsutra':
    kshar()

#...............................................................
def anusastra():
    
    
    
    st.title('AnuShastra Report')
    st.markdown('Enter All Details Below')

    select_block(a='h1')


    #name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='AnuShastra Report'):
        year = st.selectbox("Year*",options=year_list)
        block = blc
        #date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*",options= Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*",options=lt)
        nw =st.text_input(label='MARM*')
        ol =st.text_input(label='JALOKA*')
        yl = st.text_input(label="RAKTMOKSHAN*")
        rd =st.text_input(label="ALABU*")
        wh =st.text_input(label="MRITIKA*")
        bl = st.text_input(label="CUPPING*")
        nw1 =st.text_input(label='AGNIKARMA*')
        ol1 =st.text_input(label='KSHARKARMA*')


        st.markdown('**required*')
        submit_button = st.form_submit_button(label='SUBMIT Anushastra Report')
        if submit_button:
        #st.write('Submitted........')

            if not month or not year or not block or not ahc  or not yl or not rd  or not wh or not bl  or not nw1 or not ol1:
                st.warning('Ensure all fields are filled')
        # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
        #     st.warning('Select diffrent Month Entry already made')
        #     st.stop()
            else :
                ptr_data ={
                    'YEAR':int(year),
                    'BLOCK':block,
            
                    'MONTH':month,
                    'NAME OF AHC':ahc,
                    'MARM':nw,
                    'JALOKA':ol,
                    'RAKTMOKSHAN':yl,
                    'ALABU':rd,
                    'MRITIKA':wh,
                    'CUPPING':bl,
                    'AGNIKARMA':nw1,
                    'KSHARKARMA':ol1}
                data = ptr_data
                   
                    
                dbfunc(d='anu_reports',data=data,year=year,ahc=ahc,month=month)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data,index=[0]))
if selected2 == 'AnuShastra':
    anusastra()

def consolidated_ptr():
    
    st.title('Consolidated PTR Report of District Shimla')

    st.markdown('PTR Report')

    get_pt(d='reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)

def consolidated_ger_ptr():
    
    st.title('Consolidated Geriatric PTR Report of District Shimla')

    st.markdown('Geriatric PTR Report')
    get_pt(d='ger_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)


def consolidated_adhar():
    
    st.title('Consolidated Aadhar Report of District Shimla')

    st.markdown('Aadhar Report')
    get_pt(d='adahar_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)

def consolidated_bmw():
    
    st.title('Consolidated BMW Report of District Shimla')

    st.markdown('BMW Report')
    get_pt(d='bmw_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)

def consolidated_sap():
    
    st.title('Consolidated SAP Report of District Shimla')

    st.markdown('SAP Report')
    get_pt(d='sap_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)

def consolidated_tb():
    
    st.title('Consolidated TB Report of District Shimla')

    st.markdown('TB mukt Report')
    get_pt(d='tb_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)

def consolidated_pk():
    
    st.title('Consolidated Panchkarma Report of District Shimla')

    st.markdown('Panchkarma  Report')
    get_pt(d='pk_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)

def ks():
    
    st.title('Consolidated Ksharsutra Report of District Shimla')

    st.markdown('Ksharsutra  Report')
    get_pt(d='pk_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)


def anus():
    
    st.title('Consolidated Anushastra Report of District Shimla')

    st.markdown('Anushastra  Report')
    get_pt(d='anu_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)

def consolidated_po():
    
    st.title('Consolidated Poshan Report of District Shimla')

    st.markdown('Poshan Report')
    get_pt(d='poshan_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)

def consolidated_ayuhim():
    
    st.title('Consolidated Ayushman/Himcare Report of District Shimla')

    st.markdown('Ayushman/Himcare Report')
    get_pt(d='ayuhim_reports')
    
    df1 = pd.DataFrame(df)
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df,use_container_width=True)


button_select =["Monthly PTR", "Geriatric PTR", 'Aadhar Seeded / Saptahic yog','BMW','SAP','TB Mukt','Panchkarma_PTR','Ksharsutra','Anushastra','Poshan','AYUSHMAN_HIMCARE']


if selected2 == 'Consolidated Reports':
    but = st.radio('Select Option to view Total Consolidated Report',button_select,index=None,horizontal=True)
    if but == "Monthly PTR":
        consolidated_ptr()
    elif but == 'Geriatric PTR':
        consolidated_ger_ptr()
    elif but =='Aadhar Seeded / Saptahic yog':
        consolidated_adhar()
    elif but == 'BMW':
        consolidated_bmw()
    elif but =='SAP':
        consolidated_sap()
    elif but == 'TB Mukt':
        consolidated_tb()
    elif but == 'Panchkarma_PTR':
        consolidated_pk()
    elif but == 'Ksharsutra':
        ks()
    elif but =='Poshan':
        consolidated_po()
    elif but == 'AYUSHMAN_HIMCARE':
        consolidated_ayuhim()
    elif but == 'Anushastra':
        anus()
    



















    # st.title('Consolidated Report of District Shimla')
    # existingdata = conn.read(worksheet='reports',usecols=list(range(22)),ttl=5)
    # existingdata = existingdata.dropna(how='all')

    # st.markdown('TOTAL PATIENT TREATED REPORT OF DISTRICT SHIMLA')
    # df = pd.DataFrame(existingdata).transpose()
    # df = df.tail(17)
    # df['Total'] = df.sum(axis=1)
    # df = df.transpose()
    # df = df.iloc[-1:]
    # df.reset_index()
    # st.write(df)


    # df_shimla = existingdata[(existingdata['BLOCK'] == 'SHIMLA')]
    # df_sandhu = existingdata[(existingdata['BLOCK'] == 'SANDHU')]
    # df_nerwa = existingdata[(existingdata['BLOCK'] == 'NERWA')]
    # df_rampur = existingdata[(existingdata['BLOCK'] == 'RAMPUR')]
    # df_rohru = existingdata[(existingdata['BLOCK'] == 'ROHRU')]    
    # st.markdown('PTR REPORT OF SHIMLA BLOCK')
    # st.write(df_shimla)
    # st.markdown('PTR REPORT OF SANDHU BLOCK')
    # st.write(df_sandhu)
    # st.markdown('PTR REPORT OF NERWA BLOCK')
    # st.write(df_nerwa)
    # st.markdown('PTR REPORT OF RAMPUR BLOCK')
    # st.write(df_rampur)
    # st.markdown('PTR REPORT OF ROHRU BLOCK')
    # st.write(df_rohru)




