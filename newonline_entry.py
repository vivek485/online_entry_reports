import streamlit as st
from extra import *
from streamlit_option_menu import option_menu
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from appwrite.client import Client
from appwrite.services.databases import Databases

from appwrite.id import ID

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('66d67eca0028b93eb768')
client.set_key(
    'standard_6c07d1cc4f9016294c0bbc7f2e5142b0fb78aabbc9f60f12c52402192a2eb8e15c9c44ca543e879705b306d87471b26e798e3da3538a9c5982e080a0259197c8e106d1e700a9e9de635e0086fd7fbfed49133e1c2a06d98b5a7fdb28b238029f136ed839bf74303dbdd1a51da42ac906578d95afe3d820250a3477c1e6c994fb')


databases = Databases(client)


# ipdcol=['YEAR','BLOCK','MONTH','NAME OF AHC','MONTH','IPD_NEW','IPD_OLD','IPD_MALE','IPD_FEMALE','IPD_CHILD','IPD_TOTAL','Geriatric_IPD_NEW','Geriatric_IPD_OLD','Geriatric_IPD_MALE','Geriatric_IPD_FEMALE','Geriatric_IPD_CHILD','Geriatric_IPD_TOTAL']


# def get_pt_df(d):
#     global db
#     global deta
#     global df
#     # deta =
#     db = deta.Base(d)
#
#     db_content = db.fetch().items
#     if d == 'reports':
#         df = pd.DataFrame(db_content)
#         return df


def dbfunc(data, year, ahc, month, id):
    us = str(year) + "_" + str(ahc) + '_' + str(month)
    databases.create_document(
        database_id='allreports',
        collection_id=id,
        document_id=us,
        data=data
    )


def getdata(a, col):
    b = databases.list_documents(database_id='allreports', collection_id=a)
    g = b['documents']

    df = pd.DataFrame.from_dict(g, orient='columns')
    df = df[col]
    return df





def get_pt(d, col):
    global df

    if d == pt:
        b = databases.list_documents(database_id='allreports', collection_id=pt)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df
    if d == gpt:
        b = databases.list_documents(database_id='allreports', collection_id=gpt)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df
    if d == adhar:
        b = databases.list_documents(database_id='allreports', collection_id=adhar)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df
    if d == bm:
        b = databases.list_documents(database_id='allreports', collection_id=bm)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df
    if d == sap:
        b = databases.list_documents(database_id='allreports', collection_id=sap)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df
    if d == tb:
        b = databases.list_documents(database_id='allreports', collection_id=tb)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]

        return df
    if d == pk:
        b = databases.list_documents(database_id='allreports', collection_id=pk)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df
    if d == ks:
        return df
    if d == pos:
        b = databases.list_documents(database_id='allreports', collection_id=pos)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df
    if d == ayhim:
        b = databases.list_documents(database_id='allreports', collection_id=ayhim)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]

        return df
    if d == anu:
        b = databases.list_documents(database_id='allreports', collection_id=anu)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]

        return df
    if d == camps:
        b = databases.list_documents(database_id='allreports', collection_id=camps)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df
    if d == pt_ipd:
        b = databases.list_documents(database_id='allreports', collection_id=pt_ipd)
        g = b['documents']

        df = pd.DataFrame.from_dict(g, orient='columns')
        df = df[col]
        return df


st.set_page_config(layout="wide")
st.title("Reporting of District Shimla")

# -----------------------------------------------------------------------------

year_list = ['2024', '2025', '2026', '2027']
block_list = sorted(['SANDHU', 'SHIMLA', 'NERWA', 'RAMPUR', 'ROHRU'])
Month_list = ['JANUARY', 'FEBUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER',
              'NOVEMBER', 'DECEMBER']
name_ahc_shimla = sorted(
    ['HHC RAH SHIMLA', 'GALOT', 'ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA',
     'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI',
     'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA',
     'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI',
     'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR'])
name_ahc_nerwa = sorted(
    ['BAMTA', 'BHALOO', 'BHARAN', 'BHARANU', 'C/BAG', 'DHAR CHANDNA', 'HALAU', 'JORNA', 'KHAGNA', 'KHAKHARONA',
     'KIARNOO', 'MALTH', 'MAROG', 'NANHAR', 'PORIYA', 'PULBAHAL', 'SHAMTHA', 'SHILA BAWAT', 'TAILOR', 'TANDAI',
     'TIKKAR'])
name_ahc_sandhu = sorted(
    ['ALAWANG', 'BADEON', 'BAGHAL', 'BAGHI', 'BAGRI', 'CHEOG', 'DARKOTI', 'DHARONK', 'KAMAH', 'KHANETI', 'KIAR',
     'KIARTOO', 'KUTHAR', 'MAHASU', 'NAGAN', 'PADGAYA', 'PANJANA', 'PURAG', 'RAWLAKIAR', 'SANDHU', 'SAROG', 'SATOG',
     'SATANDRI', 'TIYALI'])
name_ahc_rampur = sorted(
    ['AY.HOSP.RAMPUR', 'BATHARA', 'BHAMNOLI', 'BHAROG', 'DAGYANA', 'DANSA', 'DARAN', 'DARKALI', 'DELATH', 'DOFDA',
     'DUTT NAGAR', 'GAHAN', 'GALANI', 'JAGORI', 'JAROL', 'JAWALDA', 'JUNI', 'KALEDA', 'KANDA', 'KANGAL', 'KANHAR',
     'KASHAPAT', 'KATHINE', 'KHAMADI', 'KINNU', 'KKASHAPAT', 'KOOT', 'KUHAL', 'KUNGAL BALTI', 'LABANA', 'LOUGA',
     'MAHOLI', 'MUNISH', 'NARAIN', 'NOGLI', 'PHANCHA', 'REOG', 'SANARSA', 'SARPARA', 'SHOLI', 'SURAD', 'THARU'])
name_ahc_rohru = sorted(
    ['ARHAL', 'AY.HOSP.ROHRU', 'BARARA', 'BASHTARI', 'DHAKRANTU', 'DHAR', 'GAJYANI', 'GHASNI', 'HARWANI', 'JAGTHAN',
     'JAKHAR', 'JAKHNOTI', 'JANGLIK', 'JHARAG', 'K/PATHER', 'KADIWAN', 'KHARLA', 'KHAROT', 'KUDDU', 'KUI', 'LAROT',
     'MASTOT', 'PANDRANU', 'PRAUNTHI', 'ROHAL', 'S/NAGAR', 'SALNA', 'SARIBASA', 'SAROT', 'SHEELGHAT', 'TIKKARI',
     'TURAN'])
AHWC_list = sorted(
    ['CHEOG', 'JATHIYA DEVI', 'MAHOLI', 'KANGAL', 'NOGLI', 'PANDRANU', 'SHOGHI', 'BAGHAL', 'BAGHI', 'HALAU', 'SALNA',
     'DUMMI', 'THAILA', 'KIARTOO', 'RAWLAKIAR', 'MAHASU', 'SURAD', 'SHOLI', 'BAGRI', 'SHEELGHAT', 'KHAROT', 'NABHA',
     'CHAKKAR', 'BAMTA', 'DANSA', 'LAUGA', 'DARKOTI', 'KANDA', 'DOFDA', 'BATHARA', 'MUNISH', 'NARAIN', 'KKASHAPAT',
     'DELATH', 'BHAROG', 'DUTT NAGAR', 'SARPARA', 'PHANCHA', 'KOOT', 'KHOOL', 'KALIHATTI', 'SANKATMOCHAN', 'PAHAL',
     'KHATNOL', 'KIAR', 'DAGYANA', 'GALANI', 'SATANDRI', 'KADIWAN', 'JAKHOO', 'KAITHU', 'HARWANI', 'BASHTARI', 'KUI',
     'NEW-SHIMLA', 'BEOLIA'])
lt = name_ahc_shimla
blc = 'SHIMLA'

# -------------------------------------------------------------------------
name_ahc = sorted(
    ['ANUAMBAPUR', 'AY.HOSP.ROHRU', 'AY.HOSP.RAMPUR', 'HHC RAH SHIMLA', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH',
     'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI',
     'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR',
     'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA',
     'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR',
     'BAMTA', 'BHALOO', 'BHARAN', 'BHARANU', 'C/BAG',  'DHAR CHANDNA', 'HALAU', 'JORNA', 'KHAGNA',
     'KHAKHARONA', 'KIARNOO', 'MALTH', 'MAROG', 'NANHAR', 'PORIYA', 'PULBAHAL', 'SHAMTHA', 'SHILA BAWAT',
     'TAILOR', 'TANDAI', 'TIKKAR',
     'ALAWANG', 'BADEON', 'BAGHAL', 'BAGHI', 'BAGRI', 'CHEOG', 'DARKOTI', 'DHARONK', 'KAMAH', 'KHANETI', 'KIAR',
     'KIARTOO', 'KUTHAR', 'MAHASU', 'NAGAN', 'PADGAYA', 'PANJANA', 'PURAG', 'RAWLAKIAR', 'SANDHU', 'SAROG', 'SATOG',
     'SATANDRI', 'TIYALI',
     'BATHARA', 'BHAMNOLI', 'BHAROG', 'DAGYANA', 'DANSA', 'DARAN', 'DARKALI', 'DELATH', 'DOFDA', 'DUTT NAGAR', 'GAHAN',
     'GALANI', 'JAGORI', 'JAROL', 'JAWALDA', 'JUNI', 'KALEDA', 'KANDA', 'KANGAL', 'KANHAR', 'KASHAPAT', 'KATHINE',
     'KHAMADI', 'KINNU', 'KKASHAPAT', 'KOOT', 'KUHAL', 'KUNGAL BALTI', 'LABANA', 'LOUGA', 'MAHOLI', 'MUNISH', 'NARAIN',
     'NOGLI', 'PHANCHA', 'REOG', 'SANARSA', 'SARPARA', 'SHOLI', 'SURAD', 'THARU',
     'ARHAL', 'AY.HOSP.ROHRU', 'BARARA', 'BASHTARI', 'DHAKRANTU', 'DHAR', 'GAJYANI', 'GALOT', 'GHASNI', 'HARWANI',
     'JAGTHAN', 'JAKHAR', 'JAKHNOTI', 'JANGLIK', 'JHARAG', 'K/PATHER', 'KADIWAN', 'KHARLA', 'KHAROT', 'KUDDU', 'KUI',
     'LAROT', 'MASTOT', 'PANDRANU', 'PRAUNTHI', 'ROHAL', 'S/NAGAR', 'SALNA', 'SARIBASA', 'SAROT', 'SHEELGHAT',
     'TIKKARI', 'TURAN'])


# --------------------------------------------------------------------------
def select_block(a):
    global lt
    global blc
    bloc = st.radio('Select Block for which you want to fill report', block_list, index=None, horizontal=True, key=a)
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

selected2 = option_menu("AYUSH VIBHAG HIMACHAL PRADESH",
                        ["Home", "Monthly PTR", "Geriatric PTR", 'Aadhar Seeded / Saptahic yog', 'BMW', 'SAP',
                         'TB Mukt', 'Ksharsutra', 'AnuShastra', 'Panchkarma_PTR', 'Poshan', 'AYUSHMAN_HIMCARE', 'Camps',
                         'IPD_PTR/Geriatric_PTR', 'Edit/View', 'Consolidated Reports'],
                        icons=['house', 'boxes', "boxes", 'boxes', 'boxes', 'boxes', 'boxes', 'boxes', 'boxes', 'boxes',
                               'boxes', 'boxes', 'boxes', 'boxes'],
                        menu_icon="cast", default_index=0, orientation="horizontal")


def edit_entry():
    with st.sidebar:
        # actions....................................................
        action = st.selectbox('Choose an action', ['Edit Entry', 'View Entries'])
        if action == 'View Entries':
            st.markdown('Select AHC and report to view entries made...')
            ac1 = st.selectbox('Choose from below',
                               options=["Monthly PTR", "Geriatric PTR", 'Aadhar Seeded', 'BMW', 'SAP', 'TB Mukt',
                                        'Ksharsutra', 'Panchkarma_PTR', 'Poshan', 'AYUSHMAN_HIMCARE', 'AnuShastra',
                                        'Camps', 'IPD_PTR/Geriatric_PTR'])

            if ac1 == 'Monthly PTR':
                select_block(a='a1')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=pt, col=ptrlt))
                st.write(df[df['AHC'] == ahc])
                # D = st.button("Remove Entry")
                # us = removedata(a=pt)
                # if D:
                #
                #     databases.delete_document(database_id='allreports', collection_id=pt, document_id=us)
                #     st.stop()



                # df = df[df['Name of AHC :-']== st.selectbox('select AHC',options=name_ahc)]
                # st.write(df)


            elif ac1 == 'Geriatric PTR':
                select_block(a='a2')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=gpt, col=geptrlt))
                st.write(df[df['AHC'] == ahc])
            elif ac1 == 'Aadhar Seeded':
                select_block(a='a3')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=adhar, col=adharcol))
                st.write(df[df['AHC'] == ahc])
            elif ac1 == 'BMW':
                select_block(a='a4')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=bm, col=bmwcol))
                st.write(df[df['AHC'] == ahc])
            elif ac1 == 'SAP':
                select_block(a='a5')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=sap, col=sapcol))
                st.write(df[df['AHC'] == ahc])
            elif ac1 == 'TB Mukt':
                select_block(a='a6')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=tb, col=tbcol))
                st.write(df[df['AHC'] == ahc])
            elif ac1 == 'Panchkarma_PTR':
                hosp = ['AYU_HOSPITAL_ROHRU', 'AYU_HOSPITAL_RAMPUR']

                ahc = st.selectbox('select Hospital', options=hosp)
                df = pd.DataFrame(getdata(a=pk, col=pkcol))
                st.write(df[df['AHC'] == ahc])
            elif ac1 == 'Ksharsutra':
                hosp = ['AYU_HOSPITAL_ROHRU', 'AYU_HOSPITAL_RAMPUR']

                ahc = st.selectbox('select Hospital', options=hosp)
                df = pd.DataFrame(getdata(a=ks, col=kscol))
                st.write(df[df['AHC'] == ahc])

            elif ac1 == 'Poshan':
                select_block(a='a7')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=pos, col=poshancol))
                st.write(df[df['AHC'] == ahc])
            elif ac1 == 'AYUSHMAN_HIMCARE':
                hosp = ['AYU_HOSPITAL_ROHRU', 'AYU_HOSPITAL_RAMPUR']

                ahc = st.selectbox('select Hospital', options=hosp)
                df = pd.DataFrame(getdata(a=ayhim, col=ayuhimcol))
                st.write(df[df['AHC'] == ahc])
            elif ac1 == 'AnuShastra':
                select_block(a='a8')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=anu, col=anucol))
                st.write(df[df['AHC'] == ahc])

            elif ac1 == 'Camps':
                select_block(a='a9')
                ahc = st.selectbox('select AHC', options=lt)
                df = pd.DataFrame(getdata(a=camps, col=camp))
                st.write(df)
            elif ac1 == 'IPD_PTR/Geriatric_PTR':
                hosp = ['AYU_HOSPITAL_ROHRU', 'AYU_HOSPITAL_RAMPUR']

                ahc = st.selectbox('select AHC', options=hosp)
                df = pd.DataFrame(getdata(a=pt_ipd, col=ipd_plt))
                st.write(df[df['AHC'] == ahc])
        # edit---------------------------------------------------------------------------------------------------------------------------------------

        if action == 'Edit Entry':
            st.write('## Your entry will be deleted ##')
            ac1 = st.selectbox('Choose from below',
                               options=["Monthly PTR", "Geriatric PTR", 'Aadhar Seeded', 'BMW', 'SAP', 'TB Mukt',
                                        'Ksharsutra', 'Panchkarma_PTR', 'Poshan', 'AYUSHMAN_HIMCARE', 'AnuShastra',
                                        'Camps', 'IPD_PTR/Geriatric_PTR'])

            if ac1 == 'Monthly PTR':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)


                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=pt, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=pt, document_id=us)
                        st.warning('Removed')
                except:
                    st.write("Entry not found")
            if ac1 == 'Geriatric PTR':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=gpt, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=gpt, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')
            if ac1 == 'Aadhar Seeded':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=adhar, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=adhar, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')
            if ac1 == 'BMW':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=bm, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=bm, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')
            if ac1 == 'SAP':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=sap, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=sap, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')
            if ac1 == 'TB Mukt':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=sap, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=sap, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')

            if ac1 == 'Ksharsutra':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=ks, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=ks, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')
            if ac1 == 'Panchkarma_PTR':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=pk, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=pk, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')
            if ac1 == 'Poshan':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=pos, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=pos, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')

            if ac1 == 'AYUSHMAN_HIMCARE':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=ayhim, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=ayhim, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')

            if ac1 == 'AnuShastra':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=anu, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=anu, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')

            if ac1 == 'Camps':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=camps, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=camps, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')

            if ac1 == 'IPD_PTR/Geriatric_PTR':
                try:
                    select_block(a='a1')
                    ahc = st.selectbox('select AHC', options=lt)
                    year = st.selectbox("Year*", options=year_list)
                    month = st.selectbox("Month*", options=Month_list)
                    us = str(year) + "_" + str(ahc) + '_' + str(month)
                    dtu = databases.get_document(database_id='allreports', collection_id=pt_ipd, document_id=us)
                    st.write(pd.DataFrame(dtu,columns=ptrlt,index=[0]))
                    d = st.button('Remove')
                    if d:

                        databases.delete_document(database_id='allreports', collection_id=pt_ipd, document_id=us)
                        st.warning('Removed')
                except:
                    st.warning('Entry not found kindly make entry first from main page')




if selected2 == 'Edit/View':
    edit_entry()
# selected2
w = 'Make sure to look Month column after downloading data as consolidated data will add other months data too in --- ( Total Blockwise And Total Distt.) tables.....  '


def home():
    # st.title('Reporting of District Shimla')
    st.markdown('click on above tabs to submit new reports....')
    st.divider()
    st.write(f'<h1 style="color:#fc6532;font-size:24px;">{w}</h1>', unsafe_allow_html=True)
    st.divider()
    b = st.button('Click to view Total PTR Reports till today')

    if b:
        df2 = pd.DataFrame(getdata(a=pt, col=ptrlt))
        l = ptrlt[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)

    c = st.button('Click to view Total Geriatric PTR Reports till today')
    if c:
        df2 = pd.DataFrame(getdata(a=gpt, col=geptrlt))

        l = geptrlt[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    d = st.button('Click to view Total Adhar/Yog Reports till today')
    if d:
        df2 =pd.DataFrame(getdata(a=adhar, col=adharcol))
        adharcol1 = adharcol
        l = adharcol1[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    e = st.button('Click to view Total BMW Reports till today')
    if e:

        df2 = pd.DataFrame(getdata(a=bm, col=bmwcol))
        l = bmwcol[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    # f = st.button('Click to view Total SAP Reports till today')
    # if f:
    #     df2 =pd.DataFrame(getdata(a=sap, col=sapcol))
    #     l = sapcol[-1:]
    #     df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
    #     df_count = df2[df2['TOTAL_BENEFICIARIES'] != 0].dropna()
    #     f_df = df_count.copy()
    #
    #     st.write('## Total SAP Data ##')
    #     st.dataframe(f_df)
    #     st.write('## Total Group (Month / Block) Total beneficiaries SAP Data ##')
    #     df_count2 = f_df.groupby(['BLOCK', 'MONTH'])['TOTAL_BENEFICIARIES'].sum()
    #     st.dataframe(df_count2)
    #     st.write('## Total beneficiaries SAP Data for Month ##')
    #     df_count3 = f_df.groupby(['MONTH'])['TOTAL_BENEFICIARIES'].sum()
    #     st.dataframe(df_count3)
    #     st.write('## Total Type of School visited data till now ##')
    #
    #     cot_df = f_df[(f_df['TYPE_OF_SCHOOL'] == 'Primary')]
    #     df_count9 = cot_df.groupby(['BLOCK', 'MONTH'])['TYPE_OF_SCHOOL'].count()
    #
    #     df_count_9 = pd.DataFrame(df_count9)
    #     df_count_9.rename(columns={'TYPE_OF_SCHOOL': 'PRIMARY'}, inplace=True)
    #     st.write(cot_df)
    #     # st.write(df_count_9)
    #
    #     cot_df1 = f_df[(f_df['TYPE_OF_SCHOOL'] == 'Middle')]
    #     df_count_8 = cot_df1.groupby(['BLOCK', 'MONTH'])['TYPE_OF_SCHOOL'].count()
    #     df_count_8 = pd.DataFrame(df_count_8)
    #     df_count_8.rename(columns={'TYPE_OF_SCHOOL': 'MIDDLE'}, inplace=True)
    #     st.write(cot_df1)
    #     # st.write(df_count_8)
    #
    #     cot_df2 = f_df[(f_df['TYPE_OF_SCHOOL'] == 'Sr Secondary')]
    #     df_count9_1 = cot_df2.groupby(['BLOCK', 'MONTH'])['TYPE_OF_SCHOOL'].count()
    #     df_count_9_1 = pd.DataFrame(df_count9_1)
    #     df_count_9_1.rename(columns={'TYPE_OF_SCHOOL': 'SR_SECONDARY'}, inplace=True)
    #     st.write(cot_df2)
    #     # st.write(df_count_9_1)
    #
    #     cot_df3 = f_df[(f_df['TYPE_OF_SCHOOL'] == 'Others')]
    #     df_count9_2 = cot_df3.groupby(['BLOCK', 'MONTH'])['TYPE_OF_SCHOOL'].count()
    #     df_count_9_2 = pd.DataFrame(df_count9_2)
    #     df_count_9_2.rename(columns={'TYPE_OF_SCHOOL': 'OTHERS'}, inplace=True)
    #     st.write(cot_df3)
    #     # st.write(df_count_9_2)
    #
    #     col1, col2, col3, col4 = st.columns(4)
    #
    #     with col1:
    #         st.header("Primary")
    #         st.dataframe(df_count_9)
    #
    #     with col2:
    #         st.header("Middle")
    #         st.dataframe(df_count_8)
    #
    #     with col3:
    #         st.header("Sr_Secondary")
    #         st.dataframe(df_count_9_1)
    #     with col4:
    #         st.header("Others")
    #         st.dataframe(df_count_9_2)
    #
    #     st.write('## Total type of School visited till now ##')
    #
    #     df_counting = f_df['TYPE_OF_SCHOOL'].value_counts()
    #     st.write(df_counting)

    j = st.button('Click to view Total TB Mukt Reports till today')
    if j:
        df2 = pd.DataFrame(getdata(a=tb, col=tbcol))
        tbcol1 = tbcol
        l = tbcol1[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    g = st.button('Click to view Total Panchkarma Reports till today')
    if g:
        df2 = pd.DataFrame(getdata(a=pk, col=pkcol))
        l = pkcol[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    p = st.button('Click to view Total Ksharsutra Reports till today')
    if p:
        df2 = pd.DataFrame(getdata(a=ks, col=kscol))
        l = kscol[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    h = st.button('Click to view Total Poshan Reports till today')
    if h:
        df2 = pd.DataFrame(getdata(a=pos, col=poshancol))
        l = poshancol[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    i = st.button('Click to view Total Ayushman/Himcare Reports till today')
    if i:
        df2 = pd.DataFrame(getdata(a=ayhim, col=ayuhimcol))
        l = ayuhimcol[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    m = st.button('Click to view Total Anushastra Reports till today')
    if m:
        df2 = pd.DataFrame(getdata(a=anu, col=anucol))
        l = anucol[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
    v = st.button('Click to view >300 report till today')
    if v:
        df2 = pd.DataFrame(getdata(a=pt, col=ptrlt))
        l1 = ['YEAR', 'BLOCK', 'MONTH', 'AHC', 'NEW_PATIENTS', 'OLD_PATIENTS',
              'MALE_PATIENTS', 'FEMALE_PATIENTS', 'CHILD_PATIENTS', 'TOTAL_PATIENT']
        l = l1[4:]
        df2[l] = df2[l].apply(pd.to_numeric, errors='coerce', axis=1)
        df2 = df2[df2['NEW_PATIENTS'] >= 300]

        df3 = df2.groupby(['BLOCK', 'MONTH'])[l].sum()
        df6 = df2.groupby(['BLOCK', 'MONTH', 'AHC'])['AHC'].count()
        df4 = df2.groupby(['BLOCK'])[l].sum()
        df5 = df2.groupby(['YEAR'])[l].sum()
        st.write('## Monthwise / Blockwise Data ##')
        st.dataframe(df3)
        st.write('## Total Blockwise Data ##')
        st.dataframe(df4)
        st.write('## Total Data of District ##')
        st.dataframe(df5)
        st.write('## Total AHC with opd>300 of District Shimla Blockwise ##')
        st.dataframe(df6)
    c4 = st.button('Click to view AWHC Total Patients Reports today')
    if c4:
        df_1 = pd.DataFrame(getdata(a=pt, col=ptrlt))
        # st.write(df_1)
        filtered_df = df_1[df_1['AHC'].isin(AHWC_list)]
        new_df = filtered_df.copy(deep=True)
        new_df.reset_index(inplace=True, drop=True)
        # st.dataframe(filtered_df)

        filtered_df1 = dataframe_explorer(new_df)
        st.dataframe(filtered_df1, use_container_width=True)
    v45 = st.button('Click to view Total Camps Reports')
    if v45:
        df_1 = pd.DataFrame(getdata(a=camps, col=camp))
        # st.write(df_1)

        filtered_df1 = df_1  # dataframe_explorer(df_1)
        st.dataframe(filtered_df1, use_container_width=True)

    v46 = st.button('Click to view Total IPD-PTR/Geriatric Reports')
    if v46:
        df_1 = pd.DataFrame(getdata(a=pt_ipd, col=ipd_plt))
        # st.write(df_1)

        filtered_df1 = df_1
        st.dataframe(filtered_df1, use_container_width=True)


if selected2 == 'Home':
    home()


def ptr():
    st.title('Patients Treated Reports')
    st.markdown('Enter All Details Below')

    select_block(a='a1')
    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='PTR'):
        year = st.selectbox("Year*", options=year_list)
        block = blc  # st.selectbox('Block',options=block_list)
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
        nw = st.text_input(label="New*")
        ol = st.text_input(label="Old*")
        t = st.text_input(label="Total*")
        m = st.text_input(label="Male*")
        f = st.text_input(label="Female*")
        ch = st.text_input(label="Child*")
        ts = st.text_input(label="Total_*")
        nad = st.text_input(label="Nadi*")
        pac = st.text_input(label="Pachan*")
        rak = st.text_input(label="Rakt*")
        shw = st.text_input(label="Shwashan*")
        mut = st.text_input(label="Mutra*")
        tw = st.text_input(label="Tvak*")
        er = st.text_input(label="Eye/Ear*")
        jw = st.text_input(label="Jwar*")
        ot = st.text_input(label="Other*")
        td = st.text_input(label="Total.*")
        dt = [year, block, month, ahc, nw, ol, t, m, f, ch, ts, nad, pac, rak, shw, mut, tw, er, jw, ot, td]
        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit PTR Report')

        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not nw or not ol or not t or not m or not f or not ch or not ts or not nad or not pac or not rak or not shw or not mut or not tw or not er or not jw or not ot or not td:
                st.warning('Ensure all fields are filled')




            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(ptrlt, dt))

                if ptr_data['NEW_PATIENTS'] != ptr_data['TOTAL']:
                    st.warning("Kindly check New Patients are not matching with total of Nadi Paachan...............")
                    st.stop()

                elif int(ptr_data['NEW_PATIENTS']) + int(ptr_data['OLD_PATIENTS']) != int(ptr_data['TOTAL_PATIENTS']):
                    st.warning(
                        "Kindly check Sum of New Patients and Old Patients  is not matching with Total...............")
                    st.stop()
                elif int(ptr_data['MALE_PATIENTS']) + int(ptr_data['FEMALE_PATIENTS']) + int(
                        ptr_data['CHILD_PATIENTS']) != int(ptr_data['TOTAL_PATIENT']):
                    st.warning("Kindly check Sum of Male ,Female and Child is not matching with Total...............")
                    st.stop()
                elif int(ptr_data['TOTAL_PATIENTS']) != int(ptr_data['TOTAL_PATIENT']):
                    st.warning(
                        "Kindly check Sum of Male ,Female and Child is not matching with Total of New and Old Patients...............")
                    st.stop()

                data = ptr_data

                dbfunc(data=data, year=year, ahc=ahc, month=month, id=pt)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'Monthly PTR':
    ptr()


# --------------------------------------------------------------------------------------------------------------------------------
def ipd_ptr():
    st.title('IPD PTR Report ')
    st.markdown('Enter All Details Below')

    # st.dataframe(existingdata_ad)

    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    hosp = ['AYU_HOSPITAL_ROHRU', 'AYU_HOSPITAL_RAMPUR']
    block = ['SHIMLA']
    with st.form(key='IPD Report'):
        year = st.selectbox("Year*", options=year_list)
        block = st.selectbox('Block', options=block)

        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=hosp)
        yl = st.text_input(label="IPD_NEW*")
        rd = st.text_input(label="IPD_OLD*")
        rdt = st.text_input(label="IPD_TOTAL1*")
        wh = st.text_input(label="IPD_MALE*")
        whf = st.text_input(label="IPD_FEMALE*")
        whc = st.text_input(label="IPD_CHILD*")
        bl = st.text_input(label="IPD_TOTAL*")
        yl1 = st.text_input(label="Geriatric_IPD_NEW*")
        rd1 = st.text_input(label="Geriatric_IPD_OLD*")
        rd1t = st.text_input(label="Geriatric_IPD_TOTAL1*")
        wh1 = st.text_input(label="Geriatric_IPD_MALE*")
        whf1 = st.text_input(label="Geriatric_IPD_FEMALE*")
        whc1 = st.text_input(label="Geriatric_IPD_CHILD*")
        bl1 = st.text_input(label="Geriatric_IPD_TOTAL*")
        dt = [year, block, month, ahc, yl, rd, rdt, wh, whf, whc, bl, yl1, rd1, rd1t, wh1, whf1, whc1, bl1]
        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit IPD PTR / Geriatric PTR Report')
        if submit_button:
            # st.write('Submitted........')]

            if not month or not year or not block or not ahc or not yl or not rd or not wh or not whf or not whc or not yl1 or not rd1 or not bl or not rd1 or not whf1 or not whc1 or not bl1:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(ipd_plt, dt))
                data = ptr_data

                dbfunc(data=data, year=year, ahc=ahc, month=month, id=pt_ipd)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'IPD_PTR/Geriatric_PTR':
    ipd_ptr()


# ----------------------------------------------------------------------------------------------------------------------------------
def gerptr():
    st.title('Geriatric Patients Treated Reports')
    st.markdown('Enter All Details Below')

    select_block(a='a1')
    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='ger_PTR'):
        year = st.selectbox("Year*", options=year_list)
        block = blc  # st.selectbox('Block',options=block_list)
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
        nw = st.text_input(label="New*")
        ol = st.text_input(label="Old*")
        t = st.text_input(label="Total*")
        m = st.text_input(label="Male*")
        f = st.text_input(label="Female*")
        ch = st.text_input(label="Child*")
        ts = st.text_input(label="Total_*")
        nad = st.text_input(label="Nadi*")
        pac = st.text_input(label="Pachan*")
        rak = st.text_input(label="Rakt*")
        shw = st.text_input(label="Shwashan*")
        mut = st.text_input(label="Mutra*")
        tw = st.text_input(label="Tvak*")
        er = st.text_input(label="Eye/Ear*")
        jw = st.text_input(label="Jwar*")
        ot = st.text_input(label="Other*")
        td = st.text_input(label="Total.*")
        dt = [year, block, month, ahc, nw, ol, t, m, f, ch, ts, nad, pac, rak, shw, mut, tw, er, jw, ot, td]
        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit ger PTR Report')

        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not nw or not ol or not t or not m or not f or not ch or not ts or not nad or not pac or not rak or not shw or not mut or not tw or not er or not jw or not ot or not td:
                st.warning('Ensure all fields are filled')




            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(ptrlt, dt))

                if ptr_data['NEW_PATIENTS'] != ptr_data['TOTAL']:
                    st.warning("Kindly check New Patients are not matching with total of Nadi Paachan...............")
                    st.stop()

                elif int(ptr_data['NEW_PATIENTS']) + int(ptr_data['OLD_PATIENTS']) != int(ptr_data['TOTAL_PATIENTS']):
                    st.warning(
                        "Kindly check Sum of New Patients and Old Patients  is not matching with Total...............")
                    st.stop()
                elif int(ptr_data['MALE_PATIENTS']) + int(ptr_data['FEMALE_PATIENTS']) + int(
                        ptr_data['CHILD_PATIENTS']) != int(ptr_data['TOTAL_PATIENT']):
                    st.warning("Kindly check Sum of Male ,Female and Child is not matching with Total...............")
                    st.stop()
                elif int(ptr_data['TOTAL_PATIENTS']) != int(ptr_data['TOTAL_PATIENT']):
                    st.warning(
                        "Kindly check Sum of Male ,Female and Child is not matching with Total of New and Old Patients...............")
                    st.stop()

                data = ptr_data

                dbfunc(data=data, year=year, ahc=ahc, month=month, id=gpt)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'Geriatric PTR':
    gerptr()


def adhar1():
    st.title('Aadhar Reports')
    st.markdown('Enter All Details Below')

    # st.dataframe(existingdata_ad)
    select_block(a='c1')
    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='Aadhar/yog'):
        year = st.selectbox("Year*", options=year_list)
        block = blc  # st.selectbox('Block',options=block_list)
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
        # us1 = str(year) + "_" + str(ahc) + '_' + str(month)
        ol1 = st.text_input(label="Total No. of patients attended*")
        ol_ = st.text_input(label="Total No. of MALE patients attended*")
        t_f = st.text_input(label="Total No. of FEMALE patients attended*")
        t_ = st.text_input(label="Total No. of Aadhar seeded beneficiaries*")
        m_ = st.text_input(label="Total No. of beneficiaries having Mob. No.*")
        f_ = st.text_input(label="DATE OF Yoga SESSION*")
        ch_ = st.text_input(label="TOTAL NO OF SESSION*")
        ts_ = st.text_input(label="NO OF MALE BENEFICIARY*")
        nad_ = st.text_input(label="NO OF FEMALE BENEFICIARY*")
        pac_ = st.text_input(label="NO OF CHILD BENEFICIARY*")
        pac1 = st.text_input(label="Total NO OF  Yoga BENEFICIARY*")
        dt = [year,block,month,ahc,ol1,ol_, t_f, t_, m_, f_, ch_, ts_, nad_, pac_,pac1]

        # rak_ = st.text_input(label="TOTAL NO OF YOGA BENEFICIARY IN MONTH*")

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Adhar/Yog Report')

        # checkdf = df[df['Name of AHC :-'] == ahc]
        # va = checkdf.copy()
        # van = pd.DataFrame(va,columns=['TOTAL PATIENTS'])

        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not ol_ or not t_ or not t_f or not m_ or not f_ or not ts_ or not nad_ or not pac_:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()

            else:


                ptr_data = dict(zip(adharcol, dt))
                #
                # if int(ptr_data['Total No. of MALE patients attended']) + int(
                #         ptr_data['Total No. of FEMALE patients attended']) != tp:
                #     st.warning(
                #         f"Kindly check Sum of Male ,Female is not matching with Total of value {tp}...............your sum is {nw} add or subtract {less_value} in Male/Female ")
                #     st.stop()

                data = ptr_data
                dbfunc(data=data, year=year, ahc=ahc, month=month, id=adhar)



                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))



if selected2 == 'Aadhar Seeded / Saptahic yog':
    adhar1()


def bmw():
    st.title('Bio Medical Waste Report')
    st.markdown('# Enter All Details Below donot write gms in front of value')

    # #st.dataframe(existingdata_ad)
    select_block(a='d1')
    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='BMW Report'):
        year = st.selectbox("Year*", options=year_list)
        block = blc  # st.selectbox('Block',options=block_list)
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
        yl = st.text_input(label="YELLOW CATEGORY IN GRMS*")
        rd = st.text_input(label="RED CATEGORY IN GRMS*")
        wh = st.text_input(label="WHITE CATEGORY IN GRMS*")
        bl = st.text_input(label="BLUE CATEGORY IN GRMS*")
        tl = st.text_input(label="TOTAL IN GRMS*")
        lq = st.text_input(label="LIQUID WASTE GENERATED in liters*")
        dt=[year,block,month,ahc,yl,rd,wh,bl,tl,lq]

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit BMW Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not yl or not rd or not wh or not bl or not lq:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(bmwcol, dt))
                data = ptr_data
                dbfunc(data=data, year=year, ahc=ahc, month=month, id=bm)


                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'BMW':
    bmw()


def sap1():
    st.title('School Adoption Report')
    st.markdown('Enter All Details Below')

    select_block(a='e1')
    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    school_type = ['Primary', 'Sr_Secondary', 'Middle', 'College', 'Others']
    with st.form(key='SAP Report'):
        year = st.selectbox("Year*", options=year_list)
        block = blc  # st.selectbox('Block',options=block_list)

        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
        yl = st.text_input(label="DATE OF ACTIVITY*")
        rd = st.text_input(label="NAME OF SCHOOL*")
        wh = st.selectbox("TYPE OF SCHOOL*", options=school_type)
        bl = st.text_input(label="SUBJECT COVERED*")
        tl = st.text_input(label="TOTAL BENEFICIARIES*")
        dt = [year, block, month, ahc, yl, rd, wh, bl, tl]

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit SAP Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not yl or not rd or not wh or not bl or not tl:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(sapcol, dt))

                data = ptr_data

                dbfunc(data=data, year=year, ahc=ahc, month=month, id=sap)


                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


# ------------------------------------------------total school visited
if selected2 == 'SAP':
    sap1()


def tbmukt():
    st.title('Patients TB Mukt Reports')
    st.markdown('Enter All Details Below')

    # st.dataframe(existingdata)
    select_block(a='f1')
    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='TB Mukt'):
        year = st.selectbox("Year*", options=year_list)
        block = blc  # st.selectbox('Block',options=block_list)

        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
        nw = st.text_input(label="Total monthly OPD (A)*")
        ol = st.text_input(label="New 70% Adult OPD (B)=out of A*")
        t = st.text_input(label="No. of TB suspects for sputum microscopy (C)=out of B*")
        m = st.text_input(label="Referral rate (D)=C/B x 100*")
        f = st.text_input(label="TB suspects found positive (E)=out of C*")
        ch = st.text_input(label="Name of DMCs where patient was sent for sputum test (F)*")
        ts = st.text_input(label="Total TB patients on DOTS in AHC during the reporting month (A)*")
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
        dt = [year, block, month, ahc, nw,ol,t,m,f,ch,ts,nad,pac,rak,shw,mut,tw,er,jw,ot,td]
        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit TB Mukt Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not nw or not ol or not t or not m or not f or not ch or not ts or not nad or not pac or not rak or not shw or not mut or not tw or not er or not jw or not ot or not td:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(tbcol, dt))

                data = ptr_data

                dbfunc(data=data, year=year, ahc=ahc, month=month, id=tb)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'TB Mukt':
    tbmukt()


def panchkarma_ptr():
    st.title('Panchkarma Report IPD/OPD')
    st.markdown('Enter All Details Below')

    # st.dataframe(existingdata_ad)

    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    hosp = ['AYU_HOSPITAL_ROHRU', 'AYU_HOSPITAL_RAMPUR']
    block = ['SHIMLA']
    with st.form(key='Panchkarma Report'):
        year = st.selectbox("Year*", options=year_list)
        block = st.selectbox('Block', options=block)

        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=hosp)
        yl = st.text_input(label="OPD_NEW*")
        rd = st.text_input(label="OPD_OLD*")
        wh = st.text_input(label="OPD_MALE*")
        whf = st.text_input(label="OPD_FEMALE*")
        whc = st.text_input(label="OPD_CHILD*")
        bl = st.text_input(label="OPD_TOTAL*")
        yl1 = st.text_input(label="IPD_NEW*")
        rd1 = st.text_input(label="IPD_OLD*")
        wh1 = st.text_input(label="IPD_MALE*")
        whf1 = st.text_input(label="IPD_FEMALE*")
        whc1 = st.text_input(label="IPD_CHILD*")
        bl1 = st.text_input(label="IPD_TOTAL*")
        dt = [year, block, month, ahc, yl,rd,wh,whf,whc,bl,yl1,rd1,wh1,whf1,whc1,bl1]

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Panchkarma Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not yl or not rd or not wh or not whf or not whc or not yl1 or not rd1 or not bl or not rd1 or not whf1 or not whc1 or not bl1:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(pkcol, dt))

                data = ptr_data

                dbfunc(data=data, year=year, ahc=ahc, month=month, id=pk)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'Panchkarma_PTR':
    panchkarma_ptr()


def poshan():
    st.title('Poshan Report')
    st.markdown('Enter All Details Below')

    # st.dataframe(existingdata_ad)
    select_block(a='g1')
    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']

    with st.form(key='Poshan Report'):
        year = st.selectbox("Year*", options=year_list)
        block = blc  # st.selectbox('Block',options=block_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        yl = st.text_input(label="MALE*")
        rd = st.text_input(label="FEMALE*")
        bl = st.text_input(label="CHILD*")
        tl = st.text_input(label="TOTAL*")
        dt = [year,block,ahc,month,yl,rd,bl,tl]

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Poshan Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not yl or not rd or not bl or not tl:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(poshancol, dt))
                data = ptr_data
                dbfunc(data=data, year=year, ahc=ahc, month=month, id=pos)
                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'Poshan':
    poshan()


def ayuhim1():
    st.title('Ayushman Himcare Report')
    st.markdown('Enter All Details Below')

    # st.dataframe(existingdata_ad)

    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    hosp = ['AYU_HOSPITAL_ROHRU', 'AYU_HOSPITAL_RAMPUR']
    block = ['SHIMLA']
    # #st.dataframe(existingdata_ad)

    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='Ayushman Report'):
        year = st.selectbox("Year*", options=year_list)
        block = st.selectbox('Block', options=block)
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=hosp)
        yl = st.text_input(label="AYUSHMAN_MALE*")
        rd = st.text_input(label="AYUSHMAN_FEMALE*")
        wh = st.text_input(label="AYUSHMAN_CHILD*")
        bl = st.text_input(label="AYUSHMAN_TOTAL*")
        tl = st.text_input(label="HIMCARE_MALE*")
        lq = st.text_input(label="HIMCARE_FEMALE*")
        lqc = st.text_input(label="HIMCARE_CHILD*")
        lq1 = st.text_input(label="HIMCARE_TOTAL*")
        dt =[year,block,month,ahc,yl,rd,wh,bl,tl,lq,lqc,lq1]

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='Submit Ayushman/Himcare Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not yl or not rd or not wh or not bl or not tl or not lq or not lqc or not lq1:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(ayuhimcol, dt))
                data = ptr_data
                dbfunc(data=data, year=year, ahc=ahc, month=month, id=ayhim)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'AYUSHMAN_HIMCARE':
    ayuhim1()


def kshar():
    st.title('Ksharsutra Report')
    st.markdown('Enter All Details Below')

    # st.dataframe(existingdata_ad)

    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    hosp = ['AYU_HOSPITAL_ROHRU', 'AYU_HOSPITAL_RAMPUR']
    block = ['SHIMLA']
    # #st.dataframe(existingdata_ad)

    # Month_list = ['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='Ksharsutra Report'):
        year = st.selectbox("Year*", options=year_list)
        block = st.selectbox('Block', options=block)
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=hosp)
        nw = st.text_input(label='NEW_OPD*')
        ol = st.text_input(label='OLD_OPD*')
        yl = st.text_input(label="MALE_OPD*")
        rd = st.text_input(label="FEMALE_OPD*")
        wh = st.text_input(label="CHILD_OPD*")
        bl = st.text_input(label="TOTAL_OPD*")
        nw1 = st.text_input(label='NEW_IPD*')
        ol1 = st.text_input(label='OLD_IPD*')
        tl = st.text_input(label="MALE_IPD*")
        lq = st.text_input(label="FEMALE_IPD*")
        lqc = st.text_input(label="CHILD_IPD*")
        lq1 = st.text_input(label="TOTAL_IPD*")
        dt =[year,block,month,ahc,nw,ol,yl,rd,wh,bl,nw1,ol1,tl,lq,lqc,lq1]

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='SUBMIT KSHARSUTRA Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not yl or not rd or not wh or not bl or not tl or not lq or not lqc or not lq1 or not nw or not nw1 or not ol or not ol1:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(kscol, dt))
                data = ptr_data
                dbfunc(data=data, year=year, ahc=ahc, month=month, id=ks)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'Ksharsutra':
    kshar()


# ...............................................................
def anusastra():
    st.title('AnuShastra Report')
    st.markdown('Enter All Details Below')

    select_block(a='h1')

    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='AnuShastra Report'):
        year = st.selectbox("Year*", options=year_list)
        block = blc
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
        nw = st.text_input(label='MARM*')
        ol = st.text_input(label='JALOKA*')
        yl = st.text_input(label="RAKTMOKSHAN*")
        rd = st.text_input(label="ALABU*")
        wh = st.text_input(label="MRITIKA*")
        bl = st.text_input(label="CUPPING*")
        nw1 = st.text_input(label='AGNIKARMA*')
        ol1 = st.text_input(label='KSHARKARMA*')
        dt =[year,block,month,ahc,nw,ol,yl,rd,wh,bl,nw1,ol1]

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='SUBMIT Anushastra Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not ahc or not yl or not rd or not wh or not bl or not nw1 or not ol1:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(anucol, dt))
                data = ptr_data
                dbfunc(data=data, year=year, ahc=ahc, month=month, id=anu)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'AnuShastra':
    anusastra()


# -------------------------------------------------------
def camps1():
    st.title('Camps Report')
    st.markdown('Enter All Details Below')

    select_block(a='h12')

    # name_ahc = ['ANUAMBAPUR', 'BALOG', 'BALOG', 'BANUTI DEVI', 'BEOLIA', 'BEUNTH', 'BHALOH', 'BHARARA', 'BHARARI', 'CHAKKAR', 'DABRI', 'DARGI', 'DHALLI', 'DUMMI', 'HIMRI', 'HIWAN', 'JABRI', 'JAKHOO', 'JATHIYA DEVI', 'KADHARGHAT', 'KAITHU', 'KALIHATTI', 'KANLOG', 'KHATNOL', 'LOWER BAZAR', 'MAJHIWAR', 'NABHA', 'NEW-SHIMLA', 'OLD JUNGA', 'PAHAL', 'PANTHAGHATI', 'PATGEHAR', 'PEERAN', 'RAMNAGAR', 'SANDOA', 'SANKATMOCHAN', 'SATLAI', 'SHOGHI', 'THAILA', 'TOTU', 'TUTIKANDI', 'U.H.C. LOWER BAZAR']
    with st.form(key='Camps Report'):
        year = st.selectbox("Year*", options=year_list)
        block = blc
        # date = st.date_input(label="Enter Date")#,value=datetime.date(2023,1,4))
        month = st.selectbox("Month*", options=Month_list)
        ahc = blc  # st.selectbox("Name of AHC/AHWC*",options=lt)
        nw = st.text_input(label='NAME OF CAMP*')
        ol = st.text_input(label='TOTAL NO OF CAMPS*')
        yl = st.text_input(label="DATES SEPERATED BY COMMA*")
        rd = st.text_input(label="PLACE*")
        wh = st.text_input(label="MALE*")
        bl = st.text_input(label="FEMALE*")
        nw1 = st.text_input(label='CHILD*')
        ol1 = st.text_input(label='TOTAL*')
        dt =[year,block,month,ahc,nw,ol,yl,rd,wh,bl,nw1,ol1]

        st.markdown('**required*')
        submit_button = st.form_submit_button(label='SUBMIT CAMP Report')
        if submit_button:
            # st.write('Submitted........')

            if not month or not year or not block or not yl or not rd or not wh or not bl or not nw1 or not ol1:
                st.warning('Ensure all fields are filled')
            # elif existingdata['REPORT FOR MONTH OF :-'].str.contains(month).any() and existingdata['Name of AHC :-'].str.contains(ahc).any():
            #     st.warning('Select diffrent Month Entry already made')
            #     st.stop()
            else:
                ptr_data = dict(zip(camp, dt))
                data = ptr_data
                dbfunc(data=data, year=year, ahc=ahc, month=month, id=camps)

                st.success('Details Successfully Submitted')
                st.write(pd.DataFrame(data, index=[0]))


if selected2 == 'Camps':
    camps1()


# ----------------------------------------------------
def consolidated_ptr():
    st.title('Consolidated PTR Report of District Shimla')

    st.markdown('PTR Report')

    df1 = pd.DataFrame(getdata(a=pt,col=ptrlt))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def consolidated_ger_ptr():
    st.title('Consolidated Geriatric PTR Report of District Shimla')

    st.markdown('Geriatric PTR Report')
    df1 = pd.DataFrame(getdata(a=gpt, col=geptrlt))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def consolidated_adhar():
    st.title('Consolidated Aadhar Report of District Shimla')

    st.markdown('Aadhar Report')
    df1 = pd.DataFrame(getdata(a=adhar, col=adharcol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def consolidated_bmw():
    st.title('Consolidated BMW Report of District Shimla')

    st.markdown('BMW Report')
    df1 = pd.DataFrame(getdata(a=bm, col=bmwcol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def consolidated_sap():
    st.title('Consolidated SAP Report of District Shimla')

    st.markdown('SAP Report')
    df1 = pd.DataFrame(getdata(a=sap, col=sapcol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def consolidated_tb():
    st.title('Consolidated TB Report of District Shimla')

    st.markdown('TB mukt Report')
    df1 = pd.DataFrame(getdata(a=tb, col=tbcol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def consolidated_pk():
    st.title('Consolidated Panchkarma Report of District Shimla')

    st.markdown('Panchkarma  Report')
    df1 = pd.DataFrame(getdata(a=pk, col=pkcol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def ks12():
    st.title('Consolidated Ksharsutra Report of District Shimla')

    st.markdown('Ksharsutra  Report')
    df1 = pd.DataFrame(getdata(a=ks, col=kscol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)

def anus():
    st.title('Consolidated Anushastra Report of District Shimla')

    st.markdown('Anushastra  Report')
    df1 = pd.DataFrame(getdata(a=anu, col=anucol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def consolidated_po():
    st.title('Consolidated Poshan Report of District Shimla')

    st.markdown('Poshan Report')
    df1 = pd.DataFrame(getdata(a=pos, col=poshancol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def consolidated_ayuhim():
    st.title('Consolidated Ayushman/Himcare Report of District Shimla')

    st.markdown('Ayushman/Himcare Report')
    df1 = pd.DataFrame(getdata(a=ayhim, col=ayuhimcol))
    filtered_df = dataframe_explorer(df1)
    st.dataframe(filtered_df, use_container_width=True)


def notsubmitted():
    st.title('These AHCs have not submitted reports')

    st.markdown('Name of AHCs')
    rep = st.selectbox('Choose from below',
                       options=["Monthly PTR", "Geriatric PTR", 'Aadhar Seeded', 'BMW', 'SAP', 'TB Mukt', 'Poshan',
                                'AnuShastra'])

    if rep == "Monthly PTR":

        df1 = pd.DataFrame(getdata(a=pt, col=ptrlt))
        month = st.selectbox("Month*", options=Month_list)
        df1 = df1[df1['MONTH'] == month]
        name_submitted = df1['AHC']
        lst = list(name_submitted)
        notsubmit = sorted(list(set(name_ahc) - set(lst)))
        txt = (str(len(notsubmit)) + ' AHCs have not submitted reports for ' + month)
        st.write(f'<h1 style="color:#33ff33;font-size:24px;">{txt}</h1>', unsafe_allow_html=True)
        st.dataframe(notsubmit, use_container_width=True)
    elif rep == 'Geriatric PTR':
        df1 = pd.DataFrame(getdata(a=gpt, col=geptrlt))
        month = st.selectbox("Month*", options=Month_list)
        df1 = df1[df1['MONTH'] == month]
        name_submitted = df1['AHC']
        lst = list(name_submitted)
        notsubmit = sorted(list(set(name_ahc) - set(lst)))
        txt = (str(len(notsubmit)) + ' AHCs have not submitted reports for ' + month)
        st.write(f'<h1 style="color:#33ff33;font-size:24px;">{txt}</h1>', unsafe_allow_html=True)
        st.dataframe(notsubmit, use_container_width=True)


    elif rep == 'Aadhar Seeded':
        df1 = pd.DataFrame(getdata(a=adhar, col=adharcol))
        month = st.selectbox("Month*", options=Month_list)
        df1 = df1[df1['MONTH'] == month]
        name_submitted = df1['AHC']
        lst = list(name_submitted)
        notsubmit = sorted(list(set(name_ahc) - set(lst)))
        txt = (str(len(notsubmit)) + ' AHCs have not submitted reports for ' + month)
        st.write(f'<h1 style="color:#33ff33;font-size:24px;">{txt}</h1>', unsafe_allow_html=True)
        st.dataframe(notsubmit, use_container_width=True)

    elif rep == 'BMW':
        df1 = pd.DataFrame(getdata(a=bm, col=bmwcol))
        month = st.selectbox("Month*", options=Month_list)
        df1 = df1[df1['MONTH'] == month]
        name_submitted = df1['AHC']
        lst = list(name_submitted)
        notsubmit = sorted(list(set(name_ahc) - set(lst)))
        txt = (str(len(notsubmit)) + ' AHCs have not submitted reports for ' + month)
        st.write(f'<h1 style="color:#33ff33;font-size:24px;">{txt}</h1>', unsafe_allow_html=True)
        st.dataframe(notsubmit, use_container_width=True)
    elif rep == 'SAP':
        df1 = pd.DataFrame(getdata(a=sap, col=sapcol))
        month = st.selectbox("Month*", options=Month_list)
        df1 = df1[df1['MONTH'] == month]
        name_submitted = df1['AHC']
        lst = list(name_submitted)
        notsubmit = sorted(list(set(name_ahc) - set(lst)))
        txt = (str(len(notsubmit)) + ' AHCs have not submitted reports for ' + month)
        st.write(f'<h1 style="color:#33ff33;font-size:24px;">{txt}</h1>', unsafe_allow_html=True)
        st.dataframe(notsubmit, use_container_width=True)
    elif rep == 'TB Mukt':
        df1 = pd.DataFrame(getdata(a=tb, col=tbcol))
        month = st.selectbox("Month*", options=Month_list)
        df1 = df1[df1['MONTH'] == month]
        name_submitted = df1['AHC']
        lst = list(name_submitted)
        notsubmit = sorted(list(set(name_ahc) - set(lst)))
        txt = (str(len(notsubmit)) + ' AHCs have not submitted reports for ' + month)
        st.write(f'<h1 style="color:#33ff33;font-size:24px;">{txt}</h1>', unsafe_allow_html=True)
        st.dataframe(notsubmit, use_container_width=True)
    elif rep == 'Poshan':
        df1 = pd.DataFrame(getdata(a=pos, col=poshancol))
        month = st.selectbox("Month*", options=Month_list)
        df1 = df1[df1['MONTH'] == month]
        name_submitted = df1['AHC']
        lst = list(name_submitted)
        notsubmit = sorted(list(set(name_ahc) - set(lst)))
        txt = (str(len(notsubmit)) + ' AHCs have not submitted reports for ' + month)
        st.write(f'<h1 style="color:#33ff33;font-size:24px;">{txt}</h1>', unsafe_allow_html=True)
        st.dataframe(notsubmit, use_container_width=True)
    elif rep == 'AnuShastra':
        df1 = pd.DataFrame(getdata(a=anu, col=anucol))
        month = st.selectbox("Month*", options=Month_list)
        df1 = df1[df1['MONTH'] == month]
        name_submitted = df1['AHC']
        lst = list(name_submitted)
        notsubmit = sorted(list(set(name_ahc) - set(lst)))
        txt = (str(len(notsubmit)) + ' AHCs have not submitted reports for ' + month)
        st.write(f'<h1 style="color:#33ff33;font-size:24px;">{txt}</h1>', unsafe_allow_html=True)
        st.dataframe(notsubmit, use_container_width=True)


button_select = ["Monthly PTR", "Geriatric PTR", 'Aadhar Seeded / Saptahic yog', 'BMW', 'SAP', 'TB Mukt',
                 'Panchkarma_PTR', 'Ksharsutra', 'Anushastra', 'Poshan', 'AYUSHMAN_HIMCARE',
                 'View AHCs who have not submitted reports','old data']

if selected2 == 'Consolidated Reports':
    but = st.radio('Select Option to view Total Consolidated Report', button_select, index=None, horizontal=True)
    if but == "Monthly PTR":
        consolidated_ptr()
    elif but == 'Geriatric PTR':
        consolidated_ger_ptr()
    elif but == 'Aadhar Seeded / Saptahic yog':
        consolidated_adhar()
    elif but == 'BMW':
        consolidated_bmw()
    elif but == 'SAP':
        consolidated_sap()
    elif but == 'TB Mukt':
        consolidated_tb()
    elif but == 'Panchkarma_PTR':
        consolidated_pk()
    elif but == 'Ksharsutra':
        ks12()
    elif but == 'Poshan':
        consolidated_po()
    elif but == 'AYUSHMAN_HIMCARE':
        consolidated_ayuhim()
    elif but == 'Anushastra':
        anus()
    elif but == 'View AHCs who have not submitted reports':
        notsubmitted()
    elif but == 'old data':
        st.write('Adhar report')
        df = pd.read_json('adahar_reports.json')
        filtered_df = dataframe_explorer(df)
        st.dataframe(filtered_df, use_container_width=True,key='w1')

        st.write('Anushastra report')
        df1 = pd.read_json('anu_reports.json')
        filtered_df1 = dataframe_explorer(df1)
        st.dataframe(filtered_df1, use_container_width=True,key='w2')

        st.write('Ayu/Himcare report')
        df2 = pd.read_json('ayuhim_reports.json')
        filtered_df2 = dataframe_explorer(df2)
        st.dataframe(filtered_df2, use_container_width=True,key='w3')

        st.write('BMW report')
        df3 = pd.read_json('bmw_reports.json')
        filtered_df3 = dataframe_explorer(df3)
        st.dataframe(filtered_df3, use_container_width=True,key='w4')

        st.write('camps report')
        df4 = pd.read_json('camps_reports.json')
        filtered_df4 = dataframe_explorer(df4)
        st.dataframe(filtered_df4, use_container_width=True,key='w5')

        st.write('Geriatric report')
        df5 = pd.read_json('ger_reports.json')
        filtered_df5 = dataframe_explorer(df5)
        st.dataframe(filtered_df5, use_container_width=True,key='w6')

        st.write('Ksharsutra report')
        df6 = pd.read_json('ks_reports.json')
        filtered_df6 = dataframe_explorer(df6)
        st.dataframe(filtered_df6, use_container_width=True,key='w7')

        st.write('Panchkarma report')
        df7 = pd.read_json('pk_reports.json')
        filtered_df7 = dataframe_explorer(df7)
        st.dataframe(filtered_df7, use_container_width=True,key='w8')

        st.write('Poshan report')
        df8 = pd.read_json('poshan_reports.json')
        filtered_df8 = dataframe_explorer(df8)
        st.dataframe(filtered_df8, use_container_width=True,key='w9')

        st.write('IPD PTR report')
        df9 = pd.read_json('ptr_ipd_reports.json')
        filtered_df9 = dataframe_explorer(df9)
        st.dataframe(filtered_df9, use_container_width=True,key='w10')

        st.write('PTR report')
        df10 = pd.read_json('reports.json')
        filtered_df10 = dataframe_explorer(df10)
        st.dataframe(filtered_df10, use_container_width=True,key='w11')

        st.write('SAP report')
        df11 = pd.read_json('sap_reports.json')
        filtered_df11 = dataframe_explorer(df11)
        st.dataframe(filtered_df11, use_container_width=True,key='w12')

        st.write('tb report')
        df12 = pd.read_json('tb_reports.json')
        filtered_df12 = dataframe_explorer(df12)
        st.dataframe(filtered_df12, use_container_width=True,key='w13')





# def removeentry():
#
#     select_block(a='a181')
#     year = st.selectbox("Year*", options=year_list)
#     block = blc
#     ahc = st.selectbox("Name of AHC/AHWC*", options=lt)
#     month = st.selectbox("Month*", options=Month_list)
#     us = str(year) + "_" + str(ahc) + '_' + str(month)
#     databases.delete_document(database_id='allreports',collection_id=pt,document_id=us)

