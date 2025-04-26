from enum import IntFlag

import comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 as __wrapper_module__
from comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 import (
    DISPID_SOTGetStorageFileName, DISPIDSPTSI_SelectionLength,
    SPAR_Medium, SRESoundEnd, SpeechCategoryRecoProfiles,
    SECFIgnoreWidth, DISPID_SGRsDynamic, DISPID_SLGetGenerationChange,
    SPCT_SUB_DICTATION, DISPID_SPIGetText, SRESoundStart,
    SPEI_END_SR_STREAM, SP_VISEME_19, ISpeechPhraseProperty,
    SVSFParseSsml, DISPID_SPPConfidence, SpeechCategoryAudioIn,
    SGLexical, SPBO_NONE, SAFT48kHz8BitStereo, SP_VISEME_6,
    SPPHRASEELEMENT, SAFTADPCM_11kHzStereo, SPINTERFERENCE_TOOLOUD,
    DISPID_SRSSupportedLanguages, DISPID_SPEsCount, SPSVerb, SVP_4,
    SVEPrivate, DISPID_SRCRetainedAudioFormat, DISPID_SRRTimes,
    ISpeechGrammarRuleStateTransition, DISPID_SGRsCommitAndSave,
    SRAORetainAudio, DISPID_SAFGetWaveFormatEx,
    SDA_Two_Trailing_Spaces, SREPhraseStart, SRAONone,
    DISPID_SLPPhoneIds, SWPUnknownWordUnpronounceable,
    DISPID_SASCurrentSeekPosition, ISpeechDataKey, SECHighConfidence,
    ISpeechPhraseRule, ISpeechRecognizerStatus, DISPID_SLGenerationId,
    SPPS_Function, DISPID_SLAddPronunciationByPhoneIds, SBOPause,
    DISPID_SFSClose, SPRS_ACTIVE_USER_DELIMITED,
    DISPID_SRCEventInterests, DISPID_SAFSetWaveFormatEx,
    DISPID_SPRNumberOfElements, DISPID_SRGSetWordSequenceData,
    DISPID_SRRDiscardResultInfo, DISPID_SRRSetTextFeedback,
    DISPID_SRCEAudioLevel, SPCT_SLEEP, DISPID_SAStatus, SpStream,
    SVP_18, SGPronounciation, SPCS_ENABLED, SGLexicalNoSpecialChars,
    eLEXTYPE_PRIVATE13, UINT_PTR, SAFTCCITT_uLaw_8kHzMono,
    SAFTCCITT_uLaw_22kHzStereo, DISPID_SFSOpen,
    DISPID_SVIsUISupported, SpeechEngineProperties, ISpGrammarBuilder,
    SAFTADPCM_22kHzStereo, SPPS_Interjection,
    SPEI_PROPERTY_NUM_CHANGE, DISPID_SLRemovePronunciation,
    SPEI_START_INPUT_STREAM, DISPID_SRGDictationUnload,
    SpeechRegistryUserRoot, SPAR_Low, SAFT16kHz16BitStereo,
    DISPID_SRRGetXMLErrorInfo, SPEI_FALSE_RECOGNITION,
    SAFT22kHz16BitMono, SAFT32kHz16BitStereo, SVSFPurgeBeforeSpeak,
    DISPID_SGRSTWeight, SPLO_DYNAMIC, ISpeechPhraseElements,
    ISpRecognizer3, DISPID_SVPause, SITooLoud, SVP_5,
    SPPHRASEREPLACEMENT, DISPID_SPEEngineConfidence, SVPOver,
    STSF_CommonAppData, DISPID_SOTs_NewEnum, DISPID_SRGDictationLoad,
    VARIANT_BOOL, DISPID_SRCEAdaptation, DISPID_SRGRecoContext,
    DISPID_SPACommit, SPRST_INACTIVE, DISPID_SDKDeleteValue,
    _LARGE_INTEGER, SPPS_NotOverriden, eLEXTYPE_PRIVATE9,
    DISPID_SVVoice, DISPID_SOTRemoveStorageFileName,
    SpeechTokenValueCLSID, SAFTCCITT_uLaw_44kHzMono, HRESULT,
    ISpSerializeState, DISPID_SGRSTNextState, SPSFunction,
    SAFTCCITT_ALaw_44kHzStereo, SAFTCCITT_uLaw_44kHzStereo,
    SAFTGSM610_8kHzMono, SpeechPropertyResourceUsage,
    DISPID_SRRTTickCount, SREStateChange, SPEI_RECO_OTHER_CONTEXT,
    ISpeechRecoResult, SVPNormal, SRERequestUI, DISPID_SRCResume,
    ISpRecoContext2, DISPID_SRCState, SAFTCCITT_ALaw_11kHzMono,
    eLEXTYPE_PRIVATE18, DISPID_SRGCmdSetRuleState, SPWORD,
    DISPID_SVSPhonemeId, ISpeechRecoContext, DISPID_SPAPhraseInfo,
    SVSFlagsAsync, DISPID_SRRAudioFormat, SVEPhoneme, SRADynamic,
    _check_version, SAFTCCITT_uLaw_11kHzMono, SAFTADPCM_11kHzMono,
    SPEI_PHRASE_START, DISPID_SREmulateRecognition, SVSFParseSapi,
    SP_VISEME_1, DISPID_SRGSetTextSelection, ISpeechPhraseAlternates,
    DISPID_SOTCGetDataKey, DISPID_SDKEnumKeys, SINoise,
    SDKLCurrentUser, ISpeechPhraseReplacements, SWTAdded, SVP_8,
    SVP_12, SPSHT_OTHER, DISPID_SPIProperties, SGDSActive,
    SP_VISEME_11, SpShortcut, typelib_path, SVP_9,
    SAFT11kHz8BitStereo, SVF_Stressed, SPEI_SR_RETAINEDAUDIO,
    SVEAllEvents, ISpRecoGrammar2, SSSPTRelativeToEnd,
    SPWP_KNOWN_WORD_PRONOUNCEABLE, _FILETIME, eLEXTYPE_RESERVED10,
    SAFTText, DISPID_SGRId, DISPID_SABIMinNotification, ISpDataKey,
    ISpStreamFormat, DISPIDSPTSI_SelectionOffset, SAFT8kHz8BitStereo,
    SVSFNLPMask, SpeechDictationTopicSpelling, DISPID_SRCBookmark,
    SpeechUserTraining, SECLowConfidence, DISPID_SLPsItem, SPAS_PAUSE,
    DISPID_SCSBaseStream, STCAll, SPCS_DISABLED,
    ISpObjectTokenCategory, SLODynamic, SVP_19, SRSInactive,
    DISPID_SPIAudioSizeTime, SPRST_ACTIVE, DISPIDSPTSI_ActiveOffset,
    IServiceProvider, SPEI_RESERVED1, DISPID_SPIAudioSizeBytes,
    ISpeechPhoneConverter, SVP_14, SVSFVoiceMask, SGRSTTRule,
    ISpAudio, DISPID_SRCERecognitionForOtherContext,
    DISPID_SOTCEnumerateTokens, DISPID_SWFESamplesPerSec, SPSHT_EMAIL,
    SpeechPropertyResponseSpeed, GUID, eLEXTYPE_PRIVATE11,
    DISPID_SGRSTText, SAFTTrueSpeech_8kHz1BitMono, LONG_PTR,
    ISpeechRecoResult2, SAFTNonStandardFormat, SVSFParseMask,
    SPCT_COMMAND, SPSMF_SAPI_PROPERTIES, SpNotifyTranslator,
    SSSPTRelativeToCurrentPosition, SpSharedRecognizer,
    DISPID_SLPSymbolic, SSSPTRelativeToStart, ISpPhrase,
    eLEXTYPE_PRIVATE7, SPEI_SR_AUDIO_LEVEL, SPGS_DISABLED,
    SVEStartInputStream, ISpLexicon, DISPID_SLWWord,
    DISPID_SPRuleFirstElement, SAFT12kHz16BitStereo, SPEI_REQUEST_UI,
    ISpEventSink, SPFM_OPEN_READWRITE, DISPID_SOTMatchesAttributes,
    SRATopLevel, DISPID_SMSGetData, DISPID_SVRate, DISPID_SLGetWords,
    DISPID_SGRAddState, DISPID_SOTId, SITooFast, SPSNotOverriden,
    SAFT48kHz16BitStereo, SWPUnknownWordPronounceable, CoClass,
    SP_VISEME_2, SPEI_TTS_BOOKMARK, SPEI_ACTIVE_CATEGORY_CHANGED,
    DISPID_SVGetProfiles, SPRS_INACTIVE, SpeechVoiceSkipTypeSentence,
    DISPID_SRCEPropertyStringChange, DISPID_SLPPartOfSpeech,
    eLEXTYPE_PRIVATE17, SPPROPERTYINFO, eLEXTYPE_VENDORLEXICON,
    SP_VISEME_16, SpeechPropertyHighConfidenceThreshold, SVEBookmark,
    ISpeechCustomStream, SPSERIALIZEDRESULT,
    SpeechAudioFormatGUIDText, SDA_One_Trailing_Space,
    SPSInterjection, DISPID_SVEBookmark, SVP_3, SPPS_Verb,
    SAFTADPCM_22kHzMono, SSTTDictation, eWORDTYPE_ADDED,
    DISPID_SRCEPropertyNumberChange, SVP_13,
    DISPID_SPEAudioStreamOffset, DISPID_SPERetainedStreamOffset,
    SP_VISEME_5, SVF_None, SPEI_UNDEFINED, DISPID_SAFGuid,
    SP_VISEME_7, SPAUDIOBUFFERINFO, SRADefaultToActive,
    SAFTGSM610_22kHzMono, SRSActive, SAFT16kHz8BitMono,
    SpeechMicTraining, DISPID_SRCVoice, ISpRecoGrammar,
    SRSInactiveWithPurge, DISPID_SPRulesItem, DISPID_SPPValue,
    SPAR_High, IEnumSpObjectTokens, SDA_No_Trailing_Space,
    ISpeechPhraseProperties, DISPID_SASetState, DISPID_SWFEFormatTag,
    eWORDTYPE_DELETED, DISPID_SLGetPronunciations, DISPID_SRRTLength,
    SpeechAudioVolume, ISpeechTextSelectionInformation,
    SSFMOpenReadWrite, SpResourceManager,
    ISpPhoneticAlphabetSelection, SDKLLocalMachine, SVP_6,
    DISPID_SPRFirstElement, DISPID_SPEsItem, SRSActiveAlways,
    eLEXTYPE_PRIVATE2, DISPID_SGRSRule, DISPID_SOTDisplayUI,
    SECNormalConfidence, SGDSActiveUserDelimited, SAFT32kHz16BitMono,
    SGDSActiveWithAutoPause, DISPID_SGRSTs_NewEnum,
    DISPID_SVESentenceBoundary, SPEI_ADAPTATION, SpCustomStream,
    SPAR_Unknown, Library, SRTExtendableParse, SAFT12kHz16BitMono,
    SAFT12kHz8BitStereo, SINoSignal, SITooQuiet, eLEXTYPE_PRIVATE15,
    SP_VISEME_9, _RemotableHandle, IInternetSecurityMgrSite,
    DISPID_SOTSetId, DISPID_SVSpeakCompleteEvent, DISPID_SVSkip,
    ISpeechObjectToken, ISpPhraseAlt, SPTEXTSELECTIONINFO,
    DISPID_SRSNumberOfActiveRules, DISPID_SGRAddResource,
    SAFT16kHz16BitMono, DISPID_SRGCmdLoadFromFile, IStream,
    DISPID_SRCEPhraseStart, SPEI_SR_BOOKMARK, DISPID_SPPId,
    DISPID_SPIElements, DISPID_SGRsItem, DISPID_SRCEFalseRecognition,
    SPFM_OPEN_READONLY, SAFTGSM610_44kHzMono, SPEI_PHONEME,
    SAFTNoAssignedFormat, DISPID_SPRuleName,
    DISPID_SLRemovePronunciationByPhoneIds, STSF_FlagCreate,
    DISPID_SVSCurrentStreamNumber, DISPID_SLWsItem,
    SAFTADPCM_8kHzMono, DISPID_SLWPronunciations, eLEXTYPE_PRIVATE6,
    DISPID_SRCPause, WSTRING, SPPS_Noun, DISPID_SPRuleChildren,
    SAFT12kHz8BitMono, DISPID_SRGetPropertyNumber,
    ISpeechRecoResultTimes, SpInProcRecoContext,
    DISPID_SOTIsUISupported, DISPID_SVSRunningState, DISPID_SLWsCount,
    SBONone, SSFMCreate, DISPID_SRGReset, SpMMAudioEnum, SPSLMA,
    SPAS_STOP, SPXRO_SML, DISPID_SRCEHypothesis, DISPID_SOTCategory,
    tagSPPROPERTYINFO, ISpeechBaseStream, SPAS_RUN,
    DISPID_SVSLastStreamNumberQueued, SPBINARYGRAMMAR,
    SAFT22kHz16BitStereo, SECFIgnoreCase, SRSEIsSpeaking,
    DISPID_SVSInputWordPosition, DISPID_SRSClsidEngine,
    eLEXTYPE_PRIVATE10, DISPID_SOTsItem,
    ISpeechGrammarRuleStateTransitions, SECFNoSpecialChars, SGDisplay,
    DISPID_SRAllowAudioInputFormatChangesOnNextSet,
    eLEXTYPE_RESERVED8, DISPID_SMSALineId, DISPID_SPIReplacements,
    DISPID_SPRuleConfidence, DISPID_SGRSTType,
    SPRS_ACTIVE_WITH_AUTO_PAUSE, SLTApp,
    DISPID_SASCurrentDevicePosition, SPWT_PRONUNCIATION,
    SPWORDPRONUNCIATIONLIST, DISPID_SRRAudio, SpCompressedLexicon,
    SFTSREngine, ISpVoice, SPEI_RESERVED3, DISPID_SVEStreamStart,
    SPEI_SOUND_END, SGSDisabled, DISPID_SABufferNotifySize,
    SSFMCreateForWrite, ISpeechAudio, SVP_0, DISPID_SGRClear,
    ISpeechWaveFormatEx, DISPID_SVEAudioLevel, SVSFIsFilename,
    DISPID_SVSLastBookmark, SAFT44kHz8BitMono, Speech_Default_Weight,
    IEnumString, eLEXTYPE_USER, ISpeechLexiconPronunciation,
    DISPID_SASNonBlockingIO, SPINTERFERENCE_LATENCY_TRUNCATE_END,
    DISPID_SGRName, DISPID_SLWType, SPDKL_LocalMachine,
    STCInprocHandler, SPEI_RECO_STATE_CHANGE, DISPID_SPAs_NewEnum,
    SPEI_TTS_AUDIO_LEVEL, SpPhraseInfoBuilder,
    DISPID_SRSCurrentStreamPosition, ISpeechPhraseAlternate,
    SAFT11kHz8BitMono, SAFT24kHz8BitStereo, ISpeechRecognizer,
    SRERecognition, tagSPTEXTSELECTIONINFO, DISPID_SAFType,
    SPVPRI_ALERT, SPEI_RECOGNITION, SWPKnownWordPronounceable,
    DISPID_SPIEngineId, DISPID_SPPFirstElement, DISPID_SPIRule,
    DISPID_SVGetVoices, SDTRule, SPVPRI_NORMAL,
    DISPID_SWFEBitsPerSample, SpPhoneConverter, SVP_7, SPVOICESTATUS,
    SVEWordBoundary, DISPID_SPEPronunciation,
    SpTextSelectionInformation, SVSFDefault, DISPID_SRRRecoContext,
    DISPID_SPILanguageId, DISPID_SPRuleId, dispid,
    DISPID_SOTGetAttribute, SpeechPropertyNormalConfidenceThreshold,
    SpeechCategoryAudioOut, SAFT8kHz8BitMono, DISPID_SVEWord,
    DISPIDSPTSI_ActiveLength, eLEXTYPE_RESERVED6, SPEI_RESERVED2,
    DISPID_SGRSTRule, SDTPronunciation, SPCT_SUB_COMMAND,
    DISPID_SLWLangId, DISPID_SRAudioInputStream, DISPID_SGRSTsItem,
    SPAO_RETAIN_AUDIO, SGSExclusive, BSTR, DISPID_SRCVoicePurgeEvent,
    DISPID_SADefaultFormat, SAFT11kHz16BitStereo, SECFDefault,
    DISPID_SVSyncronousSpeakTimeout, SpObjectToken, ISpStream,
    DISPID_SRAllowVoiceFormatMatchingOnNextSet, SREStreamStart,
    DISPID_SRSAudioStatus, DISPID_SLPsCount, SDTDisplayText,
    DISPID_SVResume, SpVoice, SVP_11, SP_VISEME_15, SVP_16,
    SpeechTokenKeyAttributes, SPEI_MAX_SR, STSF_LocalAppData,
    SVSFUnusedFlags, DISPID_SRGetFormat, SSTTWildcard,
    DISPID_SRCEEndStream, SDTProperty, SPINTERFERENCE_NONE,
    SPPS_Unknown, DISPID_SPRuleParent, SpeechAudioFormatGUIDWave,
    DISPID_SRGDictationSetState, DISPID_SPPs_NewEnum,
    SpeechAudioProperties, DISPID_SRGCmdLoadFromProprietaryGrammar,
    SpMMAudioIn, ISpeechLexiconWord, SVP_17, SpeechAddRemoveWord,
    ISpeechMemoryStream, DISPID_SRSetPropertyString, SDTLexicalForm,
    DISPID_SRCERecognizerStateChange, DISPID_SPIGetDisplayAttributes,
    SAFT48kHz16BitMono, DISPID_SRProfile, ISpMMSysAudio,
    ISpeechAudioStatus, DISPID_SPRulesCount,
    ISpeechLexiconPronunciations, eLEXTYPE_LETTERTOSOUND,
    SpeechTokenKeyFiles, SPWORDLIST, SASRun, SGSEnabled,
    DISPID_SRAudioInput, Speech_Max_Pron_Length, DISPID_SVVolume,
    SREHypothesis, SPWF_SRENGINE, DISPID_SLAddPronunciation,
    SP_VISEME_20, SDKLCurrentConfig, SAFT22kHz8BitMono,
    eLEXTYPE_PRIVATE8, SpeechAllElements,
    DISPID_SPRuleNumberOfElements, DISPID_SBSRead, SLTUser,
    DISPID_SPPNumberOfElements, DISPID_SOTsCount, ISpObjectWithToken,
    SAFT32kHz8BitStereo, ISpeechMMSysAudio, DISPID_SBSSeek,
    SpUnCompressedLexicon, IInternetSecurityManager,
    SPRST_INACTIVE_WITH_PURGE, SpeechRegistryLocalMachineRoot,
    SSFMOpenForRead, SPEI_SENTENCE_BOUNDARY, SVSFIsNotXML,
    DISPID_SPERetainedSizeBytes, SSTTTextBuffer, SPRST_NUM_STATES,
    DISPID_SPAStartElementInResult, SPDKL_CurrentConfig,
    DISPID_SGRsAdd, ISpRecognizer,
    DISPID_SRCAudioInInterferenceStatus,
    DISPID_SRGCmdLoadFromResource, SPVPRI_OVER, SVEAudioLevel,
    DISPID_SVDisplayUI, DISPID_SRGState, DISPID_SVGetAudioInputs,
    DISPID_SVPriority, DISPID_SVEVoiceChange,
    SpeechPropertyAdaptationOn, SPRECOGNIZERSTATUS, SRTSMLTimeout,
    DISPID_SPANumberOfElementsInResult, SPAUDIOSTATUS,
    DISPID_SGRSAddRuleTransition, DISPID_SRRPhraseInfo, SP_VISEME_8,
    SPSUnknown, DISPID_SRCRetainedAudio, _ISpeechRecoContextEvents,
    SPSHORTCUTPAIR, DISPID_SPCLangId,
    SpeechGrammarTagUnlimitedDictation, ISpPhoneticAlphabetConverter,
    DISPID_SRRAlternates, ISpNotifyTranslator, DISPID_SPCPhoneToId,
    SAFTGSM610_11kHzMono, DISPID_SVSLastBookmarkId,
    ISpeechPhraseRules, STSF_AppData, DISPID_SVEventInterests,
    SPEI_SR_PRIVATE, SpMMAudioOut, DISPID_SDKDeleteKey,
    DISPID_SBSWrite, DISPID_SRGCmdSetRuleIdState, DISPID_SGRsCommit,
    DISPID_SDKGetlongValue, SAFT44kHz16BitStereo, SPRS_ACTIVE,
    SREPropertyStringChange, SPEI_RESERVED6, SPINTERFERENCE_NOSIGNAL,
    SpeechPropertyLowConfidenceThreshold, DISPID_SDKSetBinaryValue,
    SAFTADPCM_44kHzStereo, DISPID_SPPEngineConfidence,
    SPXRO_Alternates_SML, ISpeechPhraseElement, SINone,
    DISPID_SVStatus, DISPID_SRCERequestUI, SPINTERFERENCE_NOISE,
    ISpShortcut, ISpeechGrammarRuleState, SPEI_RESERVED5,
    DISPID_SPEActualConfidence, DISPID_SRCreateRecoContext,
    DISPID_SPIGrammarId, Speech_Max_Word_Length, eLEXTYPE_PRIVATE20,
    DISPID_SPRText, SP_VISEME_10, SpInprocRecognizer, SPGS_EXCLUSIVE,
    SREInterference, ISpeechVoice, DISPID_SLPLangId,
    DISPID_SGRs_NewEnum, SPINTERFERENCE_LATENCY_WARNING,
    SDTReplacement, DISPID_SRCEBookmark, DISPID_SPRsItem,
    DISPID_SABIEventBias, SGDSInactive, DISPID_SGRSTsCount,
    DISPID_SWFEChannels, DISPID_SPERequiredConfidence,
    SPRECOCONTEXTSTATUS, DISPID_SRIsUISupported, ISpPhoneConverter,
    DISPID_SPRuleEngineConfidence, DISPID_SPEAudioSizeTime,
    SPWT_LEXICAL, SVPAlert, SPEI_VOICE_CHANGE, DISPID_SPEDisplayText,
    SPBO_TIME_UNITS, DISPID_SVAllowAudioOuputFormatChangesOnNextSet,
    DISPID_SWFEAvgBytesPerSec, wireHWND, DISPID_SPEAudioSizeBytes,
    ISequentialStream, SAFTCCITT_uLaw_8kHzStereo,
    SAFTCCITT_ALaw_8kHzMono, SpLexicon, eLEXTYPE_MORPHOLOGY,
    DISPID_SRCCreateResultFromMemory, DISPID_SLPType, ISpRecoContext,
    SVP_1, eLEXTYPE_PRIVATE16, ISpeechAudioBufferInfo,
    ISpResourceManager, ISpeechPhraseInfoBuilder, DISPID_SMSADeviceId,
    SVEEndInputStream, SDKLDefaultLocation, SPPS_RESERVED4,
    DISPID_SRState, DISPID_SRCEEnginePrivate,
    SPEI_PROPERTY_STRING_CHANGE, DISPID_SABIBufferSize,
    SPDKL_DefaultLocation, DISPID_SPCIdToPhone, SPSHT_Unknown,
    SPEVENT, SpFileStream, DISPID_SGRSTPropertyValue,
    SpeechCategoryVoices, DISPID_SOTCSetId, SRAInterpreter,
    DISPID_SPISaveToMemory, SpeechCategoryAppLexicons,
    DISPID_SPIEnginePrivateData, ISpStreamFormatConverter, SRAImport,
    DISPID_SGRSTPropertyId, SREBookmark, DISPID_SGRsCount,
    DISPID_SPAsItem, SpeechPropertyComplexResponseSpeed,
    SREPropertyNumChange, DISPID_SPAsCount, Speech_StreamPos_RealTime,
    DISPMETHOD, SAFTCCITT_ALaw_44kHzMono,
    DISPID_SPIAudioStreamPosition, DISPID_SLWs_NewEnum, SRSEDone,
    DISPID_SRCRequestedUIType, SDTAll, STCRemoteServer,
    DISPID_SWFEExtraData, DISPID_SPPBRestorePhraseFromMemory,
    SPPHRASEPROPERTY, DISPID_SVSpeak, SRARoot, SP_VISEME_12,
    SpeechCategoryPhoneConverters, DISPID_SOTCId, DISPID_SPPsCount,
    SPSModifier, SVP_15, SPPS_SuppressWord, SAFT44kHz16BitMono,
    SGRSTTTextBuffer, DISPID_SRSetPropertyNumber, SPEI_SOUND_START,
    SWTDeleted, SRTReSent, SDA_Consume_Leading_Spaces,
    ISpeechGrammarRule, SpMemoryStream, SREStreamEnd,
    DISPID_SVGetAudioOutputs, SGRSTTWord, DISPID_SPEDisplayAttributes,
    SPLO_STATIC, SVSFParseAutodetect, SGRSTTWildcard, SPFM_NUM_MODES,
    SAFT24kHz16BitMono, SLOStatic, DISPID_SRRSpeakAudio,
    STCLocalServer, SAFT32kHz8BitMono, SPEI_MIN_TTS, SPSNoun,
    DISPID_SRGetPropertyString, SPBO_AHEAD, SPBO_PAUSE,
    SPWORDPRONUNCIATION, SECFEmulateResult, SPRULE, SP_VISEME_14,
    eLEXTYPE_PRIVATE14, ULONG_PTR, DISPID_SPRules_NewEnum,
    SREAudioLevel, _ULARGE_INTEGER, tagSTATSTG, SASStop,
    eLEXTYPE_PRIVATE19, ISpeechXMLRecoResult, ISpeechLexicon,
    SAFT48kHz8BitMono, SRTEmulated, DISPID_SRGId, DISPID_SRCESoundEnd,
    SRTAutopause, SPGS_ENABLED, DISPID_SGRSTPropertyName, SVP_10,
    DISPID_SGRsFindRule, DISPID_SVAudioOutputStream,
    SAFTADPCM_44kHzMono, SPSSuppressWord, DISPID_SPPName,
    DISPID_SRIsShared, DISPID_SRGCmdLoadFromObject,
    DISPID_SPEs_NewEnum, ISpProperties, SDTAlternates,
    DISPID_SDKSetStringValue, DISPID_SABufferInfo, SP_VISEME_17,
    SVSFNLPSpeakPunc, DISPID_SOTCDefault, ISpEventSource, SVP_21,
    SPINTERFERENCE_TOOQUIET, eLEXTYPE_RESERVED4,
    DISPID_SDKGetBinaryValue, DISPID_SLPs_NewEnum,
    __MIDL___MIDL_itf_sapi_0000_0020_0002, SVSFPersistXML,
    SAFT8kHz16BitStereo, SGRSTTEpsilon, SRCS_Enabled, SPEI_MIN_SR,
    DISPID_SRRGetXMLResult, DISPID_SGRSTransitions,
    DISPID_SPEAudioTimeOffset, DISPID_SDKCreateKey, SVEViseme,
    SITooSlow, DISPID_SVSInputSentencePosition, ISpeechResourceLoader,
    ISpObjectToken, _ISpeechVoiceEvents, DISPID_SVSLastResult,
    SPPHRASERULE, SPFM_CREATE_ALWAYS, ISpeechLexiconWords,
    DISPID_SRGRules, SPSMF_SRGS_SEMANTICINTERPRETATION_MS,
    DISPID_SPPChildren, SpPhoneticAlphabetConverter,
    DISPID_SVEStreamEnd, SVEVoiceChange, DISPID_SOTDataKey,
    DISPID_SGRAttributes, DISPID_SRRecognizer, SASPause,
    ISpNotifySource, DISPID_SRStatus, SAFT22kHz8BitStereo, SDTAudio,
    SPEI_INTERFERENCE, SPINTERFERENCE_TOOFAST, SGRSTTDictation,
    ISpeechFileStream, SVP_2, DISPID_SVSInputSentenceLength,
    SPWF_INPUT, _lcid, eLEXTYPE_USER_SHORTCUT, DISPID_SRRTStreamTime,
    SP_VISEME_18, DISPID_SPRDisplayAttributes, SPAS_CLOSED,
    DISPID_SRCEStartStream, DISPID_SRGCmdLoadFromMemory,
    DISPID_SVSInputWordLength, DISPID_SOTGetDescription,
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN, SPSEMANTICERRORINFO,
    DISPID_SRGIsPronounceable, SREAdaptation,
    DISPID_SRSCurrentStreamNumber, SRCS_Disabled,
    DISPID_SGRInitialState, DISPID_SDKOpenKey, ISpeechGrammarRules,
    SPEI_START_SR_STREAM, DISPID_SPIStartTime, SpWaveFormatEx,
    eLEXTYPE_RESERVED7, ISpRecoCategory, SPPHRASE, SASClosed,
    eLEXTYPE_PRIVATE4, DISPID_SRCESoundStart, SFTInput,
    SpeechGrammarTagWildcard, ISpeechVoiceStatus,
    SPEI_END_INPUT_STREAM, SPPS_LMA, DISPID_SDKGetStringValue,
    SPCT_DICTATION, DISPID_SVAudioOutput, ISpeechAudioFormat,
    DISPID_SDKSetLongValue, SREFalseRecognition,
    SpeechCategoryRecognizers, SAFTCCITT_ALaw_11kHzStereo,
    SAFT24kHz16BitStereo, Speech_StreamPos_Asap,
    SAFTCCITT_ALaw_22kHzMono, DISPID_SRCRecognizer,
    eLEXTYPE_RESERVED9, SPEI_TTS_PRIVATE, SAFT8kHz16BitMono,
    SpStreamFormatConverter, COMMETHOD, DISPID_SRCCmdMaxAlternates,
    SpeechTokenKeyUI, SVSFIsXML, DISPID_SRRTOffsetFromStart,
    SRAExport, DISPID_SVEEnginePrivate, SAFTCCITT_ALaw_22kHzStereo,
    ISpXMLRecoResult, SP_VISEME_3, IUnknown, SREAllEvents,
    SVESentenceBoundary, SAFT44kHz8BitStereo, DISPID_SPPsItem,
    SPEI_WORD_BOUNDARY, DISPID_SRGCommit, SECFIgnoreKanaType,
    DISPID_SRRSaveToMemory, DISPID_SRCCreateGrammar,
    SPRECORESULTTIMES, SVP_20, SPWT_DISPLAY, ISpeechPhraseReplacement,
    DISPID_SAEventHandle, ISpeechRecoResultDispatch,
    SPSHT_NotOverriden, __MIDL___MIDL_itf_sapi_0000_0020_0001,
    ISpeechPhraseInfo, DISPID_SVSVisemeId, VARIANT, DISPID_SPRsCount,
    SPSMF_UPS, ISpeechObjectTokens, ISpeechRecoGrammar,
    SAFTCCITT_uLaw_22kHzMono, SRERecoOtherContext,
    DISPID_SRCERecognition, eLEXTYPE_PRIVATE3,
    DISPID_SOTCreateInstance, eLEXTYPE_APP, SpAudioFormat,
    SPEI_MAX_TTS, SPPS_Modifier, SRTStandard, ISpNotifySink,
    SpeechVoiceCategoryTTSRate, SAFTExtendedAudioFormat,
    SPEVENTSOURCEINFO, SpeechGrammarTagDictation,
    SpObjectTokenCategory, SPRST_ACTIVE_ALWAYS,
    DISPID_SASFreeBufferSpace, STCInprocServer, SAFT16kHz8BitStereo,
    DISPID_SPPParent, DISPID_SPELexicalForm, SpSharedRecoContext,
    SPPS_RESERVED2, SP_VISEME_13, DISPID_SVSpeakStream,
    DISPID_SRDisplayUI, DISPID_SPARecoResult,
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE, SP_VISEME_4, SPFM_CREATE,
    SPSERIALIZEDPHRASE, SAFT11kHz16BitMono, DISPID_SBSFormat,
    SpeechRecoProfileProperties, SPSHORTCUTPAIRLIST, DISPID_SAVolume,
    SPEI_HYPOTHESIS, DISPID_SVEViseme, SP_VISEME_21,
    SAFTCCITT_uLaw_11kHzStereo, DISPID_SGRSAddWordTransition,
    DISPID_SPRs_NewEnum, SP_VISEME_0, DISPID_SVWaitUntilDone,
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE, SpeechTokenIdUserLexicon,
    WAVEFORMATEX, eLEXTYPE_PRIVATE5, DISPID_SRCEInterference,
    SAFTCCITT_ALaw_8kHzStereo, ISpRecognizer2, SPINTERFERENCE_TOOSLOW,
    eLEXTYPE_PRIVATE12, DISPID_SMSSetData, DISPID_SRGetRecognizers,
    SVF_Emphasis, SPAO_NONE, SPWT_LEXICAL_NO_SPECIAL_CHARS,
    eLEXTYPE_PRIVATE1, SPDKL_CurrentUser, DISPID_SRCSetAdaptationData,
    SPPS_Noncontent, SPPS_RESERVED3, SREPrivate, DISPID_SVEPhoneme,
    SPSMF_SRGS_SAPIPROPERTIES, SAFTDefault, SAFTADPCM_8kHzStereo,
    DISPID_SOTRemove, DISPID_SDKEnumValues, __MIDL_IWinTypes_0009,
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C,
    DISPID_SGRSAddSpecialTransition, DISPID_SWFEBlockAlign,
    DISPID_SASState, SPPS_RESERVED1, DISPID_SMSAMMHandle,
    SpNullPhoneConverter, ISpRecoResult, SAFT24kHz8BitMono,
    helpstring, ISpeechObjectTokenCategory,
    DISPID_SPIRetainedSizeBytes, DISPID_SVAlertBoundary, SPEI_VISEME
)


class DISPID_SpeechVoiceStatus(IntFlag):
    DISPID_SVSCurrentStreamNumber = 1
    DISPID_SVSLastStreamNumberQueued = 2
    DISPID_SVSLastResult = 3
    DISPID_SVSRunningState = 4
    DISPID_SVSInputWordPosition = 5
    DISPID_SVSInputWordLength = 6
    DISPID_SVSInputSentencePosition = 7
    DISPID_SVSInputSentenceLength = 8
    DISPID_SVSLastBookmark = 9
    DISPID_SVSLastBookmarkId = 10
    DISPID_SVSPhonemeId = 11
    DISPID_SVSVisemeId = 12


class SpeechRecoEvents(IntFlag):
    SREStreamEnd = 1
    SRESoundStart = 2
    SRESoundEnd = 4
    SREPhraseStart = 8
    SRERecognition = 16
    SREHypothesis = 32
    SREBookmark = 64
    SREPropertyNumChange = 128
    SREPropertyStringChange = 256
    SREFalseRecognition = 512
    SREInterference = 1024
    SRERequestUI = 2048
    SREStateChange = 4096
    SREAdaptation = 8192
    SREStreamStart = 16384
    SRERecoOtherContext = 32768
    SREAudioLevel = 65536
    SREPrivate = 262144
    SREAllEvents = 393215


class SPWORDTYPE(IntFlag):
    eWORDTYPE_ADDED = 1
    eWORDTYPE_DELETED = 2


class SpeechGrammarWordType(IntFlag):
    SGDisplay = 0
    SGLexical = 1
    SGPronounciation = 2
    SGLexicalNoSpecialChars = 3


class SPVISEMES(IntFlag):
    SP_VISEME_0 = 0
    SP_VISEME_1 = 1
    SP_VISEME_2 = 2
    SP_VISEME_3 = 3
    SP_VISEME_4 = 4
    SP_VISEME_5 = 5
    SP_VISEME_6 = 6
    SP_VISEME_7 = 7
    SP_VISEME_8 = 8
    SP_VISEME_9 = 9
    SP_VISEME_10 = 10
    SP_VISEME_11 = 11
    SP_VISEME_12 = 12
    SP_VISEME_13 = 13
    SP_VISEME_14 = 14
    SP_VISEME_15 = 15
    SP_VISEME_16 = 16
    SP_VISEME_17 = 17
    SP_VISEME_18 = 18
    SP_VISEME_19 = 19
    SP_VISEME_20 = 20
    SP_VISEME_21 = 21


class SpeechVoiceSpeakFlags(IntFlag):
    SVSFDefault = 0
    SVSFlagsAsync = 1
    SVSFPurgeBeforeSpeak = 2
    SVSFIsFilename = 4
    SVSFIsXML = 8
    SVSFIsNotXML = 16
    SVSFPersistXML = 32
    SVSFNLPSpeakPunc = 64
    SVSFParseSapi = 128
    SVSFParseSsml = 256
    SVSFParseAutodetect = 0
    SVSFNLPMask = 64
    SVSFParseMask = 384
    SVSFVoiceMask = 511
    SVSFUnusedFlags = -512


class SpeechDiscardType(IntFlag):
    SDTProperty = 1
    SDTReplacement = 2
    SDTRule = 4
    SDTDisplayText = 8
    SDTLexicalForm = 16
    SDTPronunciation = 32
    SDTAudio = 64
    SDTAlternates = 128
    SDTAll = 255


class SPCATEGORYTYPE(IntFlag):
    SPCT_COMMAND = 0
    SPCT_DICTATION = 1
    SPCT_SLEEP = 2
    SPCT_SUB_COMMAND = 3
    SPCT_SUB_DICTATION = 4


class SPXMLRESULTOPTIONS(IntFlag):
    SPXRO_SML = 0
    SPXRO_Alternates_SML = 1


class DISPID_SpeechVoiceEvent(IntFlag):
    DISPID_SVEStreamStart = 1
    DISPID_SVEStreamEnd = 2
    DISPID_SVEVoiceChange = 3
    DISPID_SVEBookmark = 4
    DISPID_SVEWord = 5
    DISPID_SVEPhoneme = 6
    DISPID_SVESentenceBoundary = 7
    DISPID_SVEViseme = 8
    DISPID_SVEAudioLevel = 9
    DISPID_SVEEnginePrivate = 10


class SpeechLexiconType(IntFlag):
    SLTUser = 1
    SLTApp = 2


class SpeechPartOfSpeech(IntFlag):
    SPSNotOverriden = -1
    SPSUnknown = 0
    SPSNoun = 4096
    SPSVerb = 8192
    SPSModifier = 12288
    SPSFunction = 16384
    SPSInterjection = 20480
    SPSLMA = 28672
    SPSSuppressWord = 61440


class SPGRAMMARWORDTYPE(IntFlag):
    SPWT_DISPLAY = 0
    SPWT_LEXICAL = 1
    SPWT_PRONUNCIATION = 2
    SPWT_LEXICAL_NO_SPECIAL_CHARS = 3


class SPLOADOPTIONS(IntFlag):
    SPLO_STATIC = 0
    SPLO_DYNAMIC = 1


class SPRULESTATE(IntFlag):
    SPRS_INACTIVE = 0
    SPRS_ACTIVE = 1
    SPRS_ACTIVE_WITH_AUTO_PAUSE = 3
    SPRS_ACTIVE_USER_DELIMITED = 4


class SPWORDPRONOUNCEABLE(IntFlag):
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE = 0
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE = 1
    SPWP_KNOWN_WORD_PRONOUNCEABLE = 2


class SPGRAMMARSTATE(IntFlag):
    SPGS_DISABLED = 0
    SPGS_ENABLED = 1
    SPGS_EXCLUSIVE = 3


class SpeechDisplayAttributes(IntFlag):
    SDA_No_Trailing_Space = 0
    SDA_One_Trailing_Space = 2
    SDA_Two_Trailing_Spaces = 4
    SDA_Consume_Leading_Spaces = 8


class SpeechEngineConfidence(IntFlag):
    SECLowConfidence = -1
    SECNormalConfidence = 0
    SECHighConfidence = 1


class SpeechEmulationCompareFlags(IntFlag):
    SECFIgnoreCase = 1
    SECFIgnoreKanaType = 65536
    SECFIgnoreWidth = 131072
    SECFNoSpecialChars = 536870912
    SECFEmulateResult = 1073741824
    SECFDefault = 196609


class DISPID_SpeechRecognizer(IntFlag):
    DISPID_SRRecognizer = 1
    DISPID_SRAllowAudioInputFormatChangesOnNextSet = 2
    DISPID_SRAudioInput = 3
    DISPID_SRAudioInputStream = 4
    DISPID_SRIsShared = 5
    DISPID_SRState = 6
    DISPID_SRStatus = 7
    DISPID_SRProfile = 8
    DISPID_SREmulateRecognition = 9
    DISPID_SRCreateRecoContext = 10
    DISPID_SRGetFormat = 11
    DISPID_SRSetPropertyNumber = 12
    DISPID_SRGetPropertyNumber = 13
    DISPID_SRSetPropertyString = 14
    DISPID_SRGetPropertyString = 15
    DISPID_SRIsUISupported = 16
    DISPID_SRDisplayUI = 17
    DISPID_SRGetRecognizers = 18
    DISPID_SVGetAudioInputs = 19
    DISPID_SVGetProfiles = 20


class SPSHORTCUTTYPE(IntFlag):
    SPSHT_NotOverriden = -1
    SPSHT_Unknown = 0
    SPSHT_EMAIL = 4096
    SPSHT_OTHER = 8192
    SPPS_RESERVED1 = 12288
    SPPS_RESERVED2 = 16384
    SPPS_RESERVED3 = 20480
    SPPS_RESERVED4 = 61440


class SpeechSpecialTransitionType(IntFlag):
    SSTTWildcard = 1
    SSTTDictation = 2
    SSTTTextBuffer = 3


class SpeechAudioState(IntFlag):
    SASClosed = 0
    SASStop = 1
    SASPause = 2
    SASRun = 3


class SPSEMANTICFORMAT(IntFlag):
    SPSMF_SAPI_PROPERTIES = 0
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS = 1
    SPSMF_SRGS_SAPIPROPERTIES = 2
    SPSMF_UPS = 4
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C = 8


class SpeechVoiceEvents(IntFlag):
    SVEStartInputStream = 2
    SVEEndInputStream = 4
    SVEVoiceChange = 8
    SVEBookmark = 16
    SVEWordBoundary = 32
    SVEPhoneme = 64
    SVESentenceBoundary = 128
    SVEViseme = 256
    SVEAudioLevel = 512
    SVEPrivate = 32768
    SVEAllEvents = 33790


class DISPID_SpeechRecoContextEvents(IntFlag):
    DISPID_SRCEStartStream = 1
    DISPID_SRCEEndStream = 2
    DISPID_SRCEBookmark = 3
    DISPID_SRCESoundStart = 4
    DISPID_SRCESoundEnd = 5
    DISPID_SRCEPhraseStart = 6
    DISPID_SRCERecognition = 7
    DISPID_SRCEHypothesis = 8
    DISPID_SRCEPropertyNumberChange = 9
    DISPID_SRCEPropertyStringChange = 10
    DISPID_SRCEFalseRecognition = 11
    DISPID_SRCEInterference = 12
    DISPID_SRCERequestUI = 13
    DISPID_SRCERecognizerStateChange = 14
    DISPID_SRCEAdaptation = 15
    DISPID_SRCERecognitionForOtherContext = 16
    DISPID_SRCEAudioLevel = 17
    DISPID_SRCEEnginePrivate = 18


class SpeechRecoContextState(IntFlag):
    SRCS_Disabled = 0
    SRCS_Enabled = 1


class DISPID_SpeechRecognizerStatus(IntFlag):
    DISPID_SRSAudioStatus = 1
    DISPID_SRSCurrentStreamPosition = 2
    DISPID_SRSCurrentStreamNumber = 3
    DISPID_SRSNumberOfActiveRules = 4
    DISPID_SRSClsidEngine = 5
    DISPID_SRSSupportedLanguages = 6


class DISPID_SpeechRecoContext(IntFlag):
    DISPID_SRCRecognizer = 1
    DISPID_SRCAudioInInterferenceStatus = 2
    DISPID_SRCRequestedUIType = 3
    DISPID_SRCVoice = 4
    DISPID_SRAllowVoiceFormatMatchingOnNextSet = 5
    DISPID_SRCVoicePurgeEvent = 6
    DISPID_SRCEventInterests = 7
    DISPID_SRCCmdMaxAlternates = 8
    DISPID_SRCState = 9
    DISPID_SRCRetainedAudio = 10
    DISPID_SRCRetainedAudioFormat = 11
    DISPID_SRCPause = 12
    DISPID_SRCResume = 13
    DISPID_SRCCreateGrammar = 14
    DISPID_SRCCreateResultFromMemory = 15
    DISPID_SRCBookmark = 16
    DISPID_SRCSetAdaptationData = 17


class SPFILEMODE(IntFlag):
    SPFM_OPEN_READONLY = 0
    SPFM_OPEN_READWRITE = 1
    SPFM_CREATE = 2
    SPFM_CREATE_ALWAYS = 3
    SPFM_NUM_MODES = 4


class DISPIDSPRG(IntFlag):
    DISPID_SRGId = 1
    DISPID_SRGRecoContext = 2
    DISPID_SRGState = 3
    DISPID_SRGRules = 4
    DISPID_SRGReset = 5
    DISPID_SRGCommit = 6
    DISPID_SRGCmdLoadFromFile = 7
    DISPID_SRGCmdLoadFromObject = 8
    DISPID_SRGCmdLoadFromResource = 9
    DISPID_SRGCmdLoadFromMemory = 10
    DISPID_SRGCmdLoadFromProprietaryGrammar = 11
    DISPID_SRGCmdSetRuleState = 12
    DISPID_SRGCmdSetRuleIdState = 13
    DISPID_SRGDictationLoad = 14
    DISPID_SRGDictationUnload = 15
    DISPID_SRGDictationSetState = 16
    DISPID_SRGSetWordSequenceData = 17
    DISPID_SRGSetTextSelection = 18
    DISPID_SRGIsPronounceable = 19


class SpeechVisemeFeature(IntFlag):
    SVF_None = 0
    SVF_Stressed = 1
    SVF_Emphasis = 2


class SpeechVisemeType(IntFlag):
    SVP_0 = 0
    SVP_1 = 1
    SVP_2 = 2
    SVP_3 = 3
    SVP_4 = 4
    SVP_5 = 5
    SVP_6 = 6
    SVP_7 = 7
    SVP_8 = 8
    SVP_9 = 9
    SVP_10 = 10
    SVP_11 = 11
    SVP_12 = 12
    SVP_13 = 13
    SVP_14 = 14
    SVP_15 = 15
    SVP_16 = 16
    SVP_17 = 17
    SVP_18 = 18
    SVP_19 = 19
    SVP_20 = 20
    SVP_21 = 21


class SPPARTOFSPEECH(IntFlag):
    SPPS_NotOverriden = -1
    SPPS_Unknown = 0
    SPPS_Noun = 4096
    SPPS_Verb = 8192
    SPPS_Modifier = 12288
    SPPS_Function = 16384
    SPPS_Interjection = 20480
    SPPS_Noncontent = 24576
    SPPS_LMA = 28672
    SPPS_SuppressWord = 61440


class SpeechRetainedAudioOptions(IntFlag):
    SRAONone = 0
    SRAORetainAudio = 1


class DISPID_SpeechObjectToken(IntFlag):
    DISPID_SOTId = 1
    DISPID_SOTDataKey = 2
    DISPID_SOTCategory = 3
    DISPID_SOTGetDescription = 4
    DISPID_SOTSetId = 5
    DISPID_SOTGetAttribute = 6
    DISPID_SOTCreateInstance = 7
    DISPID_SOTRemove = 8
    DISPID_SOTGetStorageFileName = 9
    DISPID_SOTRemoveStorageFileName = 10
    DISPID_SOTIsUISupported = 11
    DISPID_SOTDisplayUI = 12
    DISPID_SOTMatchesAttributes = 13


class SpeechVoicePriority(IntFlag):
    SVPNormal = 0
    SVPAlert = 1
    SVPOver = 2


class SPBOOKMARKOPTIONS(IntFlag):
    SPBO_NONE = 0
    SPBO_PAUSE = 1
    SPBO_AHEAD = 2
    SPBO_TIME_UNITS = 4


class SpeechWordType(IntFlag):
    SWTAdded = 1
    SWTDeleted = 2


class DISPID_SpeechGrammarRule(IntFlag):
    DISPID_SGRAttributes = 1
    DISPID_SGRInitialState = 2
    DISPID_SGRName = 3
    DISPID_SGRId = 4
    DISPID_SGRClear = 5
    DISPID_SGRAddResource = 6
    DISPID_SGRAddState = 7


class SPVPRIORITY(IntFlag):
    SPVPRI_NORMAL = 0
    SPVPRI_ALERT = 1
    SPVPRI_OVER = 2


class DISPIDSPTSI(IntFlag):
    DISPIDSPTSI_ActiveOffset = 1
    DISPIDSPTSI_ActiveLength = 2
    DISPIDSPTSI_SelectionOffset = 3
    DISPIDSPTSI_SelectionLength = 4


class DISPID_SpeechObjectTokens(IntFlag):
    DISPID_SOTsCount = 1
    DISPID_SOTsItem = 0
    DISPID_SOTs_NewEnum = -4


class SpeechWordPronounceable(IntFlag):
    SWPUnknownWordUnpronounceable = 0
    SWPUnknownWordPronounceable = 1
    SWPKnownWordPronounceable = 2


class SpeechAudioFormatType(IntFlag):
    SAFTDefault = -1
    SAFTNoAssignedFormat = 0
    SAFTText = 1
    SAFTNonStandardFormat = 2
    SAFTExtendedAudioFormat = 3
    SAFT8kHz8BitMono = 4
    SAFT8kHz8BitStereo = 5
    SAFT8kHz16BitMono = 6
    SAFT8kHz16BitStereo = 7
    SAFT11kHz8BitMono = 8
    SAFT11kHz8BitStereo = 9
    SAFT11kHz16BitMono = 10
    SAFT11kHz16BitStereo = 11
    SAFT12kHz8BitMono = 12
    SAFT12kHz8BitStereo = 13
    SAFT12kHz16BitMono = 14
    SAFT12kHz16BitStereo = 15
    SAFT16kHz8BitMono = 16
    SAFT16kHz8BitStereo = 17
    SAFT16kHz16BitMono = 18
    SAFT16kHz16BitStereo = 19
    SAFT22kHz8BitMono = 20
    SAFT22kHz8BitStereo = 21
    SAFT22kHz16BitMono = 22
    SAFT22kHz16BitStereo = 23
    SAFT24kHz8BitMono = 24
    SAFT24kHz8BitStereo = 25
    SAFT24kHz16BitMono = 26
    SAFT24kHz16BitStereo = 27
    SAFT32kHz8BitMono = 28
    SAFT32kHz8BitStereo = 29
    SAFT32kHz16BitMono = 30
    SAFT32kHz16BitStereo = 31
    SAFT44kHz8BitMono = 32
    SAFT44kHz8BitStereo = 33
    SAFT44kHz16BitMono = 34
    SAFT44kHz16BitStereo = 35
    SAFT48kHz8BitMono = 36
    SAFT48kHz8BitStereo = 37
    SAFT48kHz16BitMono = 38
    SAFT48kHz16BitStereo = 39
    SAFTTrueSpeech_8kHz1BitMono = 40
    SAFTCCITT_ALaw_8kHzMono = 41
    SAFTCCITT_ALaw_8kHzStereo = 42
    SAFTCCITT_ALaw_11kHzMono = 43
    SAFTCCITT_ALaw_11kHzStereo = 44
    SAFTCCITT_ALaw_22kHzMono = 45
    SAFTCCITT_ALaw_22kHzStereo = 46
    SAFTCCITT_ALaw_44kHzMono = 47
    SAFTCCITT_ALaw_44kHzStereo = 48
    SAFTCCITT_uLaw_8kHzMono = 49
    SAFTCCITT_uLaw_8kHzStereo = 50
    SAFTCCITT_uLaw_11kHzMono = 51
    SAFTCCITT_uLaw_11kHzStereo = 52
    SAFTCCITT_uLaw_22kHzMono = 53
    SAFTCCITT_uLaw_22kHzStereo = 54
    SAFTCCITT_uLaw_44kHzMono = 55
    SAFTCCITT_uLaw_44kHzStereo = 56
    SAFTADPCM_8kHzMono = 57
    SAFTADPCM_8kHzStereo = 58
    SAFTADPCM_11kHzMono = 59
    SAFTADPCM_11kHzStereo = 60
    SAFTADPCM_22kHzMono = 61
    SAFTADPCM_22kHzStereo = 62
    SAFTADPCM_44kHzMono = 63
    SAFTADPCM_44kHzStereo = 64
    SAFTGSM610_8kHzMono = 65
    SAFTGSM610_11kHzMono = 66
    SAFTGSM610_22kHzMono = 67
    SAFTGSM610_44kHzMono = 68


class DISPID_SpeechDataKey(IntFlag):
    DISPID_SDKSetBinaryValue = 1
    DISPID_SDKGetBinaryValue = 2
    DISPID_SDKSetStringValue = 3
    DISPID_SDKGetStringValue = 4
    DISPID_SDKSetLongValue = 5
    DISPID_SDKGetlongValue = 6
    DISPID_SDKOpenKey = 7
    DISPID_SDKCreateKey = 8
    DISPID_SDKDeleteKey = 9
    DISPID_SDKDeleteValue = 10
    DISPID_SDKEnumKeys = 11
    DISPID_SDKEnumValues = 12


class DISPID_SpeechObjectTokenCategory(IntFlag):
    DISPID_SOTCId = 1
    DISPID_SOTCDefault = 2
    DISPID_SOTCSetId = 3
    DISPID_SOTCGetDataKey = 4
    DISPID_SOTCEnumerateTokens = 5


class SpeechRecognizerState(IntFlag):
    SRSInactive = 0
    SRSActive = 1
    SRSActiveAlways = 2
    SRSInactiveWithPurge = 3


class SpeechFormatType(IntFlag):
    SFTInput = 0
    SFTSREngine = 1


class SpeechRunState(IntFlag):
    SRSEDone = 1
    SRSEIsSpeaking = 2


class SPRECOSTATE(IntFlag):
    SPRST_INACTIVE = 0
    SPRST_ACTIVE = 1
    SPRST_ACTIVE_ALWAYS = 2
    SPRST_INACTIVE_WITH_PURGE = 3
    SPRST_NUM_STATES = 4


class SPWAVEFORMATTYPE(IntFlag):
    SPWF_INPUT = 0
    SPWF_SRENGINE = 1


class SPEVENTENUM(IntFlag):
    SPEI_UNDEFINED = 0
    SPEI_START_INPUT_STREAM = 1
    SPEI_END_INPUT_STREAM = 2
    SPEI_VOICE_CHANGE = 3
    SPEI_TTS_BOOKMARK = 4
    SPEI_WORD_BOUNDARY = 5
    SPEI_PHONEME = 6
    SPEI_SENTENCE_BOUNDARY = 7
    SPEI_VISEME = 8
    SPEI_TTS_AUDIO_LEVEL = 9
    SPEI_TTS_PRIVATE = 15
    SPEI_MIN_TTS = 1
    SPEI_MAX_TTS = 15
    SPEI_END_SR_STREAM = 34
    SPEI_SOUND_START = 35
    SPEI_SOUND_END = 36
    SPEI_PHRASE_START = 37
    SPEI_RECOGNITION = 38
    SPEI_HYPOTHESIS = 39
    SPEI_SR_BOOKMARK = 40
    SPEI_PROPERTY_NUM_CHANGE = 41
    SPEI_PROPERTY_STRING_CHANGE = 42
    SPEI_FALSE_RECOGNITION = 43
    SPEI_INTERFERENCE = 44
    SPEI_REQUEST_UI = 45
    SPEI_RECO_STATE_CHANGE = 46
    SPEI_ADAPTATION = 47
    SPEI_START_SR_STREAM = 48
    SPEI_RECO_OTHER_CONTEXT = 49
    SPEI_SR_AUDIO_LEVEL = 50
    SPEI_SR_RETAINEDAUDIO = 51
    SPEI_SR_PRIVATE = 52
    SPEI_ACTIVE_CATEGORY_CHANGED = 53
    SPEI_RESERVED5 = 54
    SPEI_RESERVED6 = 55
    SPEI_MIN_SR = 34
    SPEI_MAX_SR = 55
    SPEI_RESERVED1 = 30
    SPEI_RESERVED2 = 33
    SPEI_RESERVED3 = 63


class SPLEXICONTYPE(IntFlag):
    eLEXTYPE_USER = 1
    eLEXTYPE_APP = 2
    eLEXTYPE_VENDORLEXICON = 4
    eLEXTYPE_LETTERTOSOUND = 8
    eLEXTYPE_MORPHOLOGY = 16
    eLEXTYPE_RESERVED4 = 32
    eLEXTYPE_USER_SHORTCUT = 64
    eLEXTYPE_RESERVED6 = 128
    eLEXTYPE_RESERVED7 = 256
    eLEXTYPE_RESERVED8 = 512
    eLEXTYPE_RESERVED9 = 1024
    eLEXTYPE_RESERVED10 = 2048
    eLEXTYPE_PRIVATE1 = 4096
    eLEXTYPE_PRIVATE2 = 8192
    eLEXTYPE_PRIVATE3 = 16384
    eLEXTYPE_PRIVATE4 = 32768
    eLEXTYPE_PRIVATE5 = 65536
    eLEXTYPE_PRIVATE6 = 131072
    eLEXTYPE_PRIVATE7 = 262144
    eLEXTYPE_PRIVATE8 = 524288
    eLEXTYPE_PRIVATE9 = 1048576
    eLEXTYPE_PRIVATE10 = 2097152
    eLEXTYPE_PRIVATE11 = 4194304
    eLEXTYPE_PRIVATE12 = 8388608
    eLEXTYPE_PRIVATE13 = 16777216
    eLEXTYPE_PRIVATE14 = 33554432
    eLEXTYPE_PRIVATE15 = 67108864
    eLEXTYPE_PRIVATE16 = 134217728
    eLEXTYPE_PRIVATE17 = 268435456
    eLEXTYPE_PRIVATE18 = 536870912
    eLEXTYPE_PRIVATE19 = 1073741824
    eLEXTYPE_PRIVATE20 = -2147483648


class SpeechRecognitionType(IntFlag):
    SRTStandard = 0
    SRTAutopause = 1
    SRTEmulated = 2
    SRTSMLTimeout = 4
    SRTExtendableParse = 8
    SRTReSent = 16


class DISPID_SpeechGrammarRules(IntFlag):
    DISPID_SGRsCount = 1
    DISPID_SGRsDynamic = 2
    DISPID_SGRsAdd = 3
    DISPID_SGRsCommit = 4
    DISPID_SGRsCommitAndSave = 5
    DISPID_SGRsFindRule = 6
    DISPID_SGRsItem = 0
    DISPID_SGRs_NewEnum = -4


class SpeechGrammarState(IntFlag):
    SGSEnabled = 1
    SGSDisabled = 0
    SGSExclusive = 3


class SpeechLoadOption(IntFlag):
    SLOStatic = 0
    SLODynamic = 1


class SpeechRuleState(IntFlag):
    SGDSInactive = 0
    SGDSActive = 1
    SGDSActiveWithAutoPause = 3
    SGDSActiveUserDelimited = 4


class DISPID_SpeechGrammarRuleState(IntFlag):
    DISPID_SGRSRule = 1
    DISPID_SGRSTransitions = 2
    DISPID_SGRSAddWordTransition = 3
    DISPID_SGRSAddRuleTransition = 4
    DISPID_SGRSAddSpecialTransition = 5


class DISPID_SpeechWaveFormatEx(IntFlag):
    DISPID_SWFEFormatTag = 1
    DISPID_SWFEChannels = 2
    DISPID_SWFESamplesPerSec = 3
    DISPID_SWFEAvgBytesPerSec = 4
    DISPID_SWFEBlockAlign = 5
    DISPID_SWFEBitsPerSample = 6
    DISPID_SWFEExtraData = 7


class SPCONTEXTSTATE(IntFlag):
    SPCS_DISABLED = 0
    SPCS_ENABLED = 1


class DISPID_SpeechBaseStream(IntFlag):
    DISPID_SBSFormat = 1
    DISPID_SBSRead = 2
    DISPID_SBSWrite = 3
    DISPID_SBSSeek = 4


class DISPID_SpeechGrammarRuleStateTransition(IntFlag):
    DISPID_SGRSTType = 1
    DISPID_SGRSTText = 2
    DISPID_SGRSTRule = 3
    DISPID_SGRSTWeight = 4
    DISPID_SGRSTPropertyName = 5
    DISPID_SGRSTPropertyId = 6
    DISPID_SGRSTPropertyValue = 7
    DISPID_SGRSTNextState = 8


class DISPID_SpeechAudioFormat(IntFlag):
    DISPID_SAFType = 1
    DISPID_SAFGuid = 2
    DISPID_SAFGetWaveFormatEx = 3
    DISPID_SAFSetWaveFormatEx = 4


class SPADAPTATIONRELEVANCE(IntFlag):
    SPAR_Unknown = 0
    SPAR_Low = 1
    SPAR_Medium = 2
    SPAR_High = 3


class DISPID_SpeechGrammarRuleStateTransitions(IntFlag):
    DISPID_SGRSTsCount = 1
    DISPID_SGRSTsItem = 0
    DISPID_SGRSTs_NewEnum = -4


class DISPID_SpeechFileStream(IntFlag):
    DISPID_SFSOpen = 100
    DISPID_SFSClose = 101


class SpeechBookmarkOptions(IntFlag):
    SBONone = 0
    SBOPause = 1


class SpeechInterference(IntFlag):
    SINone = 0
    SINoise = 1
    SINoSignal = 2
    SITooLoud = 3
    SITooQuiet = 4
    SITooFast = 5
    SITooSlow = 6


class DISPID_SpeechPhraseBuilder(IntFlag):
    DISPID_SPPBRestorePhraseFromMemory = 1


class DISPID_SpeechRecoResult(IntFlag):
    DISPID_SRRRecoContext = 1
    DISPID_SRRTimes = 2
    DISPID_SRRAudioFormat = 3
    DISPID_SRRPhraseInfo = 4
    DISPID_SRRAlternates = 5
    DISPID_SRRAudio = 6
    DISPID_SRRSpeakAudio = 7
    DISPID_SRRSaveToMemory = 8
    DISPID_SRRDiscardResultInfo = 9


class DISPID_SpeechAudio(IntFlag):
    DISPID_SAStatus = 200
    DISPID_SABufferInfo = 201
    DISPID_SADefaultFormat = 202
    DISPID_SAVolume = 203
    DISPID_SABufferNotifySize = 204
    DISPID_SAEventHandle = 205
    DISPID_SASetState = 206


class DISPID_SpeechPhraseAlternate(IntFlag):
    DISPID_SPARecoResult = 1
    DISPID_SPAStartElementInResult = 2
    DISPID_SPANumberOfElementsInResult = 3
    DISPID_SPAPhraseInfo = 4
    DISPID_SPACommit = 5


class DISPID_SpeechMMSysAudio(IntFlag):
    DISPID_SMSADeviceId = 300
    DISPID_SMSALineId = 301
    DISPID_SMSAMMHandle = 302


class DISPID_SpeechXMLRecoResult(IntFlag):
    DISPID_SRRGetXMLResult = 10
    DISPID_SRRGetXMLErrorInfo = 11


class SpeechRuleAttributes(IntFlag):
    SRATopLevel = 1
    SRADefaultToActive = 2
    SRAExport = 4
    SRAImport = 8
    SRAInterpreter = 16
    SRADynamic = 32
    SRARoot = 64


class SpeechStreamSeekPositionType(IntFlag):
    SSSPTRelativeToStart = 0
    SSSPTRelativeToCurrentPosition = 1
    SSSPTRelativeToEnd = 2


class DISPID_SpeechPhraseInfo(IntFlag):
    DISPID_SPILanguageId = 1
    DISPID_SPIGrammarId = 2
    DISPID_SPIStartTime = 3
    DISPID_SPIAudioStreamPosition = 4
    DISPID_SPIAudioSizeBytes = 5
    DISPID_SPIRetainedSizeBytes = 6
    DISPID_SPIAudioSizeTime = 7
    DISPID_SPIRule = 8
    DISPID_SPIProperties = 9
    DISPID_SPIElements = 10
    DISPID_SPIReplacements = 11
    DISPID_SPIEngineId = 12
    DISPID_SPIEnginePrivateData = 13
    DISPID_SPISaveToMemory = 14
    DISPID_SPIGetText = 15
    DISPID_SPIGetDisplayAttributes = 16


class DISPID_SpeechAudioStatus(IntFlag):
    DISPID_SASFreeBufferSpace = 1
    DISPID_SASNonBlockingIO = 2
    DISPID_SASState = 3
    DISPID_SASCurrentSeekPosition = 4
    DISPID_SASCurrentDevicePosition = 5


class DISPID_SpeechRecoResultTimes(IntFlag):
    DISPID_SRRTStreamTime = 1
    DISPID_SRRTLength = 2
    DISPID_SRRTTickCount = 3
    DISPID_SRRTOffsetFromStart = 4


class DISPID_SpeechCustomStream(IntFlag):
    DISPID_SCSBaseStream = 100


class DISPID_SpeechMemoryStream(IntFlag):
    DISPID_SMSSetData = 100
    DISPID_SMSGetData = 101


class DISPID_SpeechRecoResult2(IntFlag):
    DISPID_SRRSetTextFeedback = 12


class DISPID_SpeechPhraseAlternates(IntFlag):
    DISPID_SPAsCount = 1
    DISPID_SPAsItem = 0
    DISPID_SPAs_NewEnum = -4


class DISPID_SpeechAudioBufferInfo(IntFlag):
    DISPID_SABIMinNotification = 1
    DISPID_SABIBufferSize = 2
    DISPID_SABIEventBias = 3


class DISPID_SpeechVoice(IntFlag):
    DISPID_SVStatus = 1
    DISPID_SVVoice = 2
    DISPID_SVAudioOutput = 3
    DISPID_SVAudioOutputStream = 4
    DISPID_SVRate = 5
    DISPID_SVVolume = 6
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet = 7
    DISPID_SVEventInterests = 8
    DISPID_SVPriority = 9
    DISPID_SVAlertBoundary = 10
    DISPID_SVSyncronousSpeakTimeout = 11
    DISPID_SVSpeak = 12
    DISPID_SVSpeakStream = 13
    DISPID_SVPause = 14
    DISPID_SVResume = 15
    DISPID_SVSkip = 16
    DISPID_SVGetVoices = 17
    DISPID_SVGetAudioOutputs = 18
    DISPID_SVWaitUntilDone = 19
    DISPID_SVSpeakCompleteEvent = 20
    DISPID_SVIsUISupported = 21
    DISPID_SVDisplayUI = 22


class DISPID_SpeechPhraseReplacement(IntFlag):
    DISPID_SPRDisplayAttributes = 1
    DISPID_SPRText = 2
    DISPID_SPRFirstElement = 3
    DISPID_SPRNumberOfElements = 4


class DISPID_SpeechPhraseElement(IntFlag):
    DISPID_SPEAudioTimeOffset = 1
    DISPID_SPEAudioSizeTime = 2
    DISPID_SPEAudioStreamOffset = 3
    DISPID_SPEAudioSizeBytes = 4
    DISPID_SPERetainedStreamOffset = 5
    DISPID_SPERetainedSizeBytes = 6
    DISPID_SPEDisplayText = 7
    DISPID_SPELexicalForm = 8
    DISPID_SPEPronunciation = 9
    DISPID_SPEDisplayAttributes = 10
    DISPID_SPERequiredConfidence = 11
    DISPID_SPEActualConfidence = 12
    DISPID_SPEEngineConfidence = 13


class DISPID_SpeechPhraseElements(IntFlag):
    DISPID_SPEsCount = 1
    DISPID_SPEsItem = 0
    DISPID_SPEs_NewEnum = -4


class DISPID_SpeechPhraseReplacements(IntFlag):
    DISPID_SPRsCount = 1
    DISPID_SPRsItem = 0
    DISPID_SPRs_NewEnum = -4


class SpeechDataKeyLocation(IntFlag):
    SDKLDefaultLocation = 0
    SDKLCurrentUser = 1
    SDKLLocalMachine = 2
    SDKLCurrentConfig = 5


class SPDATAKEYLOCATION(IntFlag):
    SPDKL_DefaultLocation = 0
    SPDKL_CurrentUser = 1
    SPDKL_LocalMachine = 2
    SPDKL_CurrentConfig = 5


class DISPID_SpeechPhraseProperty(IntFlag):
    DISPID_SPPName = 1
    DISPID_SPPId = 2
    DISPID_SPPValue = 3
    DISPID_SPPFirstElement = 4
    DISPID_SPPNumberOfElements = 5
    DISPID_SPPEngineConfidence = 6
    DISPID_SPPConfidence = 7
    DISPID_SPPParent = 8
    DISPID_SPPChildren = 9


class DISPID_SpeechLexiconProns(IntFlag):
    DISPID_SLPsCount = 1
    DISPID_SLPsItem = 0
    DISPID_SLPs_NewEnum = -4


class DISPID_SpeechLexiconWord(IntFlag):
    DISPID_SLWLangId = 1
    DISPID_SLWType = 2
    DISPID_SLWWord = 3
    DISPID_SLWPronunciations = 4


class DISPID_SpeechPhraseProperties(IntFlag):
    DISPID_SPPsCount = 1
    DISPID_SPPsItem = 0
    DISPID_SPPs_NewEnum = -4


class DISPID_SpeechPhraseRule(IntFlag):
    DISPID_SPRuleName = 1
    DISPID_SPRuleId = 2
    DISPID_SPRuleFirstElement = 3
    DISPID_SPRuleNumberOfElements = 4
    DISPID_SPRuleParent = 5
    DISPID_SPRuleChildren = 6
    DISPID_SPRuleConfidence = 7
    DISPID_SPRuleEngineConfidence = 8


class SPAUDIOOPTIONS(IntFlag):
    SPAO_NONE = 0
    SPAO_RETAIN_AUDIO = 1


class DISPID_SpeechPhraseRules(IntFlag):
    DISPID_SPRulesCount = 1
    DISPID_SPRulesItem = 0
    DISPID_SPRules_NewEnum = -4


class DISPID_SpeechLexicon(IntFlag):
    DISPID_SLGenerationId = 1
    DISPID_SLGetWords = 2
    DISPID_SLAddPronunciation = 3
    DISPID_SLAddPronunciationByPhoneIds = 4
    DISPID_SLRemovePronunciation = 5
    DISPID_SLRemovePronunciationByPhoneIds = 6
    DISPID_SLGetPronunciations = 7
    DISPID_SLGetGenerationChange = 8


class DISPID_SpeechLexiconWords(IntFlag):
    DISPID_SLWsCount = 1
    DISPID_SLWsItem = 0
    DISPID_SLWs_NewEnum = -4


class DISPID_SpeechLexiconPronunciation(IntFlag):
    DISPID_SLPType = 1
    DISPID_SLPLangId = 2
    DISPID_SLPPartOfSpeech = 3
    DISPID_SLPPhoneIds = 4
    DISPID_SLPSymbolic = 5


class DISPID_SpeechPhoneConverter(IntFlag):
    DISPID_SPCLangId = 1
    DISPID_SPCPhoneToId = 2
    DISPID_SPCIdToPhone = 3


class SPINTERFERENCE(IntFlag):
    SPINTERFERENCE_NONE = 0
    SPINTERFERENCE_NOISE = 1
    SPINTERFERENCE_NOSIGNAL = 2
    SPINTERFERENCE_TOOLOUD = 3
    SPINTERFERENCE_TOOQUIET = 4
    SPINTERFERENCE_TOOFAST = 5
    SPINTERFERENCE_TOOSLOW = 6
    SPINTERFERENCE_LATENCY_WARNING = 7
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN = 8
    SPINTERFERENCE_LATENCY_TRUNCATE_END = 9


class SpeechGrammarRuleStateTransitionType(IntFlag):
    SGRSTTEpsilon = 0
    SGRSTTWord = 1
    SGRSTTRule = 2
    SGRSTTDictation = 3
    SGRSTTWildcard = 4
    SGRSTTTextBuffer = 5


class _SPAUDIOSTATE(IntFlag):
    SPAS_CLOSED = 0
    SPAS_STOP = 1
    SPAS_PAUSE = 2
    SPAS_RUN = 3


class SpeechStreamFileMode(IntFlag):
    SSFMOpenForRead = 0
    SSFMOpenReadWrite = 1
    SSFMCreate = 2
    SSFMCreateForWrite = 3


class SpeechTokenContext(IntFlag):
    STCInprocServer = 1
    STCInprocHandler = 2
    STCLocalServer = 4
    STCRemoteServer = 16
    STCAll = 23


class SpeechTokenShellFolder(IntFlag):
    STSF_AppData = 26
    STSF_LocalAppData = 28
    STSF_CommonAppData = 35
    STSF_FlagCreate = 32768


SPSTREAMFORMATTYPE = SPWAVEFORMATTYPE
SPAUDIOSTATE = _SPAUDIOSTATE


__all__ = [
    'DISPID_SOTGetStorageFileName', 'DISPIDSPTSI_SelectionLength',
    'SPAR_Medium', 'DISPID_SRAllowVoiceFormatMatchingOnNextSet',
    'SREStreamStart', 'SRESoundEnd', 'DISPID_SRSAudioStatus',
    'SpeechBookmarkOptions', 'SpeechCategoryRecoProfiles',
    'DISPID_SLPsCount', 'DISPID_SpeechPhraseProperty',
    'SDTDisplayText', 'SECFIgnoreWidth', 'DISPID_SpeechLexicon',
    'DISPID_SVResume', 'DISPID_SGRsDynamic',
    'DISPID_SLGetGenerationChange', 'SpVoice', 'SPCT_SUB_DICTATION',
    'SVP_11', 'DISPID_SPIGetText', 'SP_VISEME_15', 'SpeechFormatType',
    'DISPID_SpeechAudio', 'SVP_16', 'SpeechTokenKeyAttributes',
    'SRESoundStart', 'SPEI_END_SR_STREAM', 'SP_VISEME_19',
    'SPEI_MAX_SR', 'STSF_LocalAppData', 'SpeechTokenContext',
    'SPCONTEXTSTATE', 'ISpeechPhraseProperty', 'SVSFParseSsml',
    'DISPID_SPPConfidence', 'SPINTERFERENCE', 'SVSFUnusedFlags',
    'DISPID_SRGetFormat', 'SSTTWildcard', 'SPFILEMODE',
    'SpeechEngineConfidence', 'SpeechCategoryAudioIn',
    'DISPID_SpeechVoiceEvent', 'SGLexical', 'SPBO_NONE',
    'DISPID_SRCEEndStream', 'SAFT48kHz8BitStereo', 'SP_VISEME_6',
    'SPPHRASEELEMENT', 'SDTProperty', 'DISPID_SpeechPhraseProperties',
    'SPINTERFERENCE_NONE', '_SPAUDIOSTATE', 'SPPS_Unknown',
    'SAFTADPCM_11kHzStereo', 'DISPID_SPRuleParent',
    'SPINTERFERENCE_TOOLOUD', 'DISPID_SRSSupportedLanguages',
    'DISPID_SPEsCount', 'DISPID_SpeechObjectTokenCategory', 'SPSVerb',
    'SVP_4', 'SpeechAudioFormatGUIDWave', 'SVEPrivate',
    'DISPID_SRCRetainedAudioFormat', 'DISPID_SRGDictationSetState',
    'DISPID_SRRTimes', 'DISPIDSPTSI', 'SpeechAudioProperties',
    'DISPID_SPPs_NewEnum', 'DISPID_SRGCmdLoadFromProprietaryGrammar',
    'SpMMAudioIn', 'SpeechLexiconType', 'ISpeechLexiconWord',
    'ISpeechGrammarRuleStateTransition', 'SVP_17',
    'DISPID_SGRsCommitAndSave', 'SpeechAddRemoveWord',
    'ISpeechMemoryStream', 'DISPID_SRSetPropertyString',
    'SRAORetainAudio', 'DISPID_SAFGetWaveFormatEx',
    'SDA_Two_Trailing_Spaces', 'SDTLexicalForm', 'SREPhraseStart',
    'DISPID_SRCERecognizerStateChange', 'SRAONone',
    'DISPID_SPIGetDisplayAttributes', 'DISPID_SLPPhoneIds',
    'SWPUnknownWordUnpronounceable', 'DISPID_SASCurrentSeekPosition',
    'SAFT48kHz16BitMono', 'ISpeechDataKey', 'DISPID_SRProfile',
    'SpeechRecoEvents', 'ISpMMSysAudio', 'SECHighConfidence',
    'SPGRAMMARSTATE', 'ISpeechPhraseRule', 'ISpeechRecognizerStatus',
    'ISpeechAudioStatus', 'SPPS_Function', 'DISPID_SPRulesCount',
    'DISPID_SLGenerationId', 'DISPID_SLAddPronunciationByPhoneIds',
    'ISpeechLexiconPronunciations', 'SBOPause', 'DISPID_SFSClose',
    'SPRS_ACTIVE_USER_DELIMITED', 'eLEXTYPE_LETTERTOSOUND',
    'SpeechTokenKeyFiles', 'DISPID_SRCEventInterests', 'SPWORDLIST',
    'DISPID_SAFSetWaveFormatEx', 'SASRun', 'SGSEnabled',
    'DISPID_SRAudioInput', 'DISPID_SPRNumberOfElements',
    'Speech_Max_Pron_Length', 'DISPID_SRGSetWordSequenceData',
    'SREHypothesis', 'SPWF_SRENGINE', 'DISPID_SVVolume',
    'SP_VISEME_20', 'DISPID_SRRDiscardResultInfo',
    'DISPID_SRCEAudioLevel', 'SPCT_SLEEP', 'SPGRAMMARWORDTYPE',
    'DISPID_SRRSetTextFeedback', 'SDKLCurrentConfig',
    'DISPID_SLAddPronunciation', 'DISPID_SAStatus', 'SpStream',
    'SAFT22kHz8BitMono', 'SVP_18', 'SPLEXICONTYPE',
    'SGPronounciation', 'eLEXTYPE_PRIVATE8',
    'SGLexicalNoSpecialChars', 'eLEXTYPE_PRIVATE13', 'SPCS_ENABLED',
    'UINT_PTR', 'SAFTCCITT_uLaw_8kHzMono',
    'SAFTCCITT_uLaw_22kHzStereo', 'SpeechAllElements',
    'SpeechVisemeType', 'DISPID_SPRuleNumberOfElements',
    'DISPID_SFSOpen', 'DISPID_SVIsUISupported',
    'SpeechEngineProperties', 'DISPID_SBSRead', 'ISpGrammarBuilder',
    'SAFTADPCM_22kHzStereo', 'DISPID_SpeechLexiconWords', 'SLTUser',
    'DISPID_SPPNumberOfElements', 'SPPS_Interjection',
    'SPEI_PROPERTY_NUM_CHANGE', 'DISPID_SLRemovePronunciation',
    'SPEI_START_INPUT_STREAM', 'DISPID_SOTsCount', 'SPSEMANTICFORMAT',
    'DISPID_SRGDictationUnload', 'SpeechRegistryUserRoot',
    'ISpObjectWithToken', 'SAFT32kHz8BitStereo', 'SPAR_Low',
    'ISpeechMMSysAudio', 'DISPID_SBSSeek', 'SAFT16kHz16BitStereo',
    'DISPID_SRRGetXMLErrorInfo', 'SPWORDPRONOUNCEABLE',
    'SPEI_FALSE_RECOGNITION', 'SpUnCompressedLexicon',
    'SAFT22kHz16BitMono', 'SAFT32kHz16BitStereo', 'SpObjectToken',
    'IInternetSecurityManager', 'SVSFPurgeBeforeSpeak',
    'DISPID_SGRSTWeight', 'SPRST_INACTIVE_WITH_PURGE', 'SPLO_DYNAMIC',
    'SpeechRegistryLocalMachineRoot', 'ISpeechPhraseElements',
    'ISpRecognizer3', 'SSFMOpenForRead', 'SPEI_SENTENCE_BOUNDARY',
    'DISPID_SVPause', 'SVSFIsNotXML', 'SITooLoud', 'SSTTTextBuffer',
    'SVP_5', 'SPRST_NUM_STATES', 'DISPID_SPAStartElementInResult',
    'DISPID_SGRsAdd', 'DISPID_SPERetainedSizeBytes',
    'SPDKL_CurrentConfig', 'SPPHRASEREPLACEMENT', 'ISpRecognizer',
    'DISPID_SRCAudioInInterferenceStatus',
    'DISPID_SPEEngineConfidence', 'DISPID_SRGCmdLoadFromResource',
    'SVPOver', 'SPVPRI_OVER', 'SVEAudioLevel', 'DISPID_SVDisplayUI',
    'DISPID_SRGState', 'DISPID_SVGetAudioInputs', 'DISPID_SVPriority',
    'DISPID_SVEVoiceChange', 'STSF_CommonAppData',
    'DISPID_SOTs_NewEnum', 'DISPID_SRGDictationLoad',
    'SpeechPropertyAdaptationOn', 'SPRECOGNIZERSTATUS',
    'SRTSMLTimeout', 'SPBOOKMARKOPTIONS',
    'DISPID_SPANumberOfElementsInResult', 'SpeechRecoContextState',
    'SPAUDIOSTATUS', 'DISPID_SGRSAddRuleTransition',
    'DISPID_SRRPhraseInfo', 'SPAUDIOSTATE', 'SP_VISEME_8',
    'SPSUnknown', 'DISPID_SRCEAdaptation', 'DISPID_SRCRetainedAudio',
    'DISPID_SRGRecoContext', 'DISPID_SDKDeleteValue',
    'SPSHORTCUTPAIR', 'SPRST_INACTIVE', '_ISpeechRecoContextEvents',
    'DISPID_SPACommit', 'DISPID_SPCLangId', 'SPPS_NotOverriden',
    'SpeechGrammarTagUnlimitedDictation', 'eLEXTYPE_PRIVATE9',
    'DISPID_SVVoice', 'ISpPhoneticAlphabetConverter',
    'DISPID_SOTRemoveStorageFileName', 'SpeechStreamFileMode',
    'DISPID_SRRAlternates', 'SpeechDisplayAttributes',
    'SpeechTokenValueCLSID', 'DISPID_SPCPhoneToId',
    'ISpNotifyTranslator', 'SAFTGSM610_11kHzMono',
    'SAFTCCITT_uLaw_44kHzMono', 'DISPID_SVSLastBookmarkId',
    'SPAUDIOOPTIONS', 'ISpSerializeState', 'DISPID_SGRSTNextState',
    'ISpeechPhraseRules', 'STSF_AppData', 'DISPID_SVEventInterests',
    'SPEI_SR_PRIVATE', 'SpMMAudioOut', 'DISPID_SDKDeleteKey',
    'SpeechRunState', 'DISPID_SBSWrite', 'SPSFunction',
    'SpeechRetainedAudioOptions', 'DISPID_SRGCmdSetRuleIdState',
    'DISPID_SGRsCommit', 'DISPID_SDKGetlongValue',
    'DISPID_SpeechGrammarRules', 'SAFT44kHz16BitStereo',
    'SAFTCCITT_ALaw_44kHzStereo', 'SPRS_ACTIVE',
    'SREPropertyStringChange', 'SAFTCCITT_uLaw_44kHzStereo',
    'SAFTGSM610_8kHzMono', 'SpeechPropertyResourceUsage',
    'SPEI_RESERVED6', 'SPINTERFERENCE_NOSIGNAL',
    'DISPID_SRRTTickCount', 'SREStateChange',
    'DISPID_SpeechLexiconPronunciation',
    'SpeechPropertyLowConfidenceThreshold',
    'DISPID_SDKSetBinaryValue', 'SAFTADPCM_44kHzStereo',
    'ISpeechRecoResult', 'SVPNormal', 'SPEI_RECO_OTHER_CONTEXT',
    'SRERequestUI', 'DISPID_SRCResume', 'DISPID_SPPEngineConfidence',
    'SPXRO_Alternates_SML', 'SGRSTTDictation', 'ISpRecoContext2',
    'DISPID_SpeechVoiceStatus', 'DISPID_SRCState',
    'ISpeechPhraseElement', 'SINone', 'SAFTCCITT_ALaw_11kHzMono',
    'DISPID_SVStatus', 'DISPID_SRCERequestUI', 'eLEXTYPE_PRIVATE18',
    'DISPID_SRGCmdSetRuleState', 'SPINTERFERENCE_NOISE', 'SPWORD',
    'ISpShortcut', 'DISPID_SVSPhonemeId', 'SPEI_RESERVED5',
    'ISpeechGrammarRuleState', 'DISPID_SPEActualConfidence',
    'DISPID_SRCreateRecoContext', 'DISPID_SPIGrammarId',
    'ISpeechRecoContext', 'DISPID_SPAPhraseInfo',
    'SpeechRuleAttributes', 'SVSFlagsAsync', 'Speech_Max_Word_Length',
    'DISPID_SRRAudioFormat', 'SpeechVoiceEvents', 'SVEPhoneme',
    'SRADynamic', 'eLEXTYPE_PRIVATE20', 'DISPID_SPRs_NewEnum',
    'SAFTCCITT_uLaw_11kHzMono', 'SAFTADPCM_11kHzMono',
    'SpeechGrammarWordType', 'DISPID_SPRText', 'SP_VISEME_10',
    'SPEI_PHRASE_START', 'SpeechDiscardType',
    'DISPID_SREmulateRecognition', 'SVSFParseSapi', 'SP_VISEME_1',
    'SPSTREAMFORMATTYPE', 'SpInprocRecognizer',
    'DISPID_SRGSetTextSelection', 'SpeechWordType', 'SPGS_EXCLUSIVE',
    'ISpeechPhraseAlternates', 'SREInterference', 'ISpeechVoice',
    'DISPID_SpeechAudioFormat', 'SpeechSpecialTransitionType',
    'DISPID_SLPLangId', 'DISPID_SOTCGetDataKey', 'DISPID_SDKEnumKeys',
    'DISPID_SGRs_NewEnum', 'SINoise', 'SPDATAKEYLOCATION',
    'SDKLCurrentUser', 'SDTReplacement', 'ISpeechPhraseReplacements',
    'SWTAdded', 'SPINTERFERENCE_LATENCY_WARNING',
    'DISPID_SRCEBookmark', 'SVP_8', 'SVP_12', 'DISPID_SPRsItem',
    'SPSHT_OTHER', 'DISPID_SPIProperties', 'DISPID_SABIEventBias',
    'SGDSActive', 'SP_VISEME_11', 'SGDSInactive',
    'DISPID_SGRSTsCount', 'SpShortcut', 'typelib_path', 'SVP_9',
    'DISPID_SpeechRecognizerStatus', 'SPWAVEFORMATTYPE',
    'DISPID_SWFEChannels', 'SpeechVoicePriority',
    'DISPID_SPERequiredConfidence', 'SAFT11kHz8BitStereo',
    'SVF_Stressed', 'SPEI_SR_RETAINEDAUDIO', 'SVEAllEvents',
    'DISPID_SpeechGrammarRuleStateTransition',
    'DISPID_SpeechAudioBufferInfo', 'SPRECOCONTEXTSTATUS',
    'ISpRecoGrammar2', 'SSSPTRelativeToEnd', 'DISPID_SRIsUISupported',
    'SPWP_KNOWN_WORD_PRONOUNCEABLE', 'ISpPhoneConverter',
    'eLEXTYPE_RESERVED10', 'SAFTText',
    'DISPID_SPRuleEngineConfidence', 'DISPID_SPEAudioSizeTime',
    'DISPID_SpeechRecoContextEvents', 'DISPID_SGRId',
    'DISPID_SABIMinNotification', 'SPWT_LEXICAL', 'ISpDataKey',
    'ISpStreamFormat', 'SVPAlert', 'DISPIDSPTSI_SelectionOffset',
    'SAFT8kHz8BitStereo', 'SPBO_TIME_UNITS', 'SPEI_VOICE_CHANGE',
    'DISPID_SPEDisplayText', 'SVSFNLPMask',
    'DISPID_SVAllowAudioOuputFormatChangesOnNextSet',
    'DISPID_SWFEAvgBytesPerSec', 'SpeechDictationTopicSpelling',
    'DISPID_SPEAudioSizeBytes', 'DISPID_SRCBookmark',
    'SpeechUserTraining', 'SECLowConfidence',
    'SAFTCCITT_uLaw_8kHzStereo', 'DISPID_SLPsItem',
    'DISPID_SpeechWaveFormatEx', 'SPAS_PAUSE',
    'SAFTCCITT_ALaw_8kHzMono', 'DISPID_SCSBaseStream', 'SpLexicon',
    'eLEXTYPE_MORPHOLOGY', 'DISPID_SRCCreateResultFromMemory',
    'ISpeechFileStream', 'STCAll', 'DISPID_SLPType', 'ISpRecoContext',
    'SVP_1', 'eLEXTYPE_PRIVATE16', 'ISpeechAudioBufferInfo',
    'ISpResourceManager', 'ISpeechPhraseInfoBuilder', 'SPCS_DISABLED',
    'ISpObjectTokenCategory', 'DISPID_SMSADeviceId', 'SLODynamic',
    'SVEEndInputStream', 'SVP_19', 'SpeechVisemeFeature',
    'SDKLDefaultLocation', 'SPPS_RESERVED4',
    'DISPID_SpeechXMLRecoResult', 'SRSInactive', 'DISPID_SRState',
    'DISPID_SRCEEnginePrivate', 'DISPID_SpeechRecoResult2',
    'SPEI_PROPERTY_STRING_CHANGE', 'DISPID_SABIBufferSize',
    'SPDKL_DefaultLocation', 'DISPID_SPCIdToPhone', 'SPSHT_Unknown',
    'SPRST_ACTIVE', 'SPEVENT', 'DISPIDSPTSI_ActiveOffset',
    'DISPID_SPIAudioSizeTime', 'SpFileStream',
    'DISPID_SGRSTPropertyValue', 'SpeechCategoryVoices',
    'DISPID_SOTCSetId', 'SRAInterpreter', 'DISPID_SPISaveToMemory',
    'SpeechCategoryAppLexicons', 'DISPID_SPIEnginePrivateData',
    'SPEI_RESERVED1', 'DISPID_SPIAudioSizeBytes',
    'ISpStreamFormatConverter', 'ISpeechPhoneConverter', 'SVP_14',
    'SVSFVoiceMask', 'DISPID_SGRSTPropertyId', 'SRAImport',
    'SGRSTTRule', 'ISpAudio', 'SREBookmark', 'DISPID_SGRsCount',
    'DISPID_SPAsItem', 'SpeechGrammarRuleStateTransitionType',
    'SpeechPropertyComplexResponseSpeed', 'SREPropertyNumChange',
    'DISPID_SPAsCount', 'Speech_StreamPos_RealTime',
    'DISPID_SRCERecognitionForOtherContext',
    'DISPID_SOTCEnumerateTokens', 'DISPID_SWFESamplesPerSec',
    'SPSHT_EMAIL', 'SpeechPropertyResponseSpeed',
    'SAFTCCITT_ALaw_44kHzMono', 'DISPID_SPIAudioStreamPosition',
    'DISPID_SLWs_NewEnum', 'eLEXTYPE_PRIVATE11', 'DISPID_SGRSTText',
    'DISPID_SpeechPhraseInfo', 'SAFTTrueSpeech_8kHz1BitMono',
    'DISPID_SRCRequestedUIType', 'SDTAll', 'SRSEDone',
    'DISPID_SWFEExtraData', 'LONG_PTR',
    'DISPID_SPPBRestorePhraseFromMemory', 'ISpeechRecoResult2',
    'STCRemoteServer', 'SPPHRASEPROPERTY', 'SAFTNonStandardFormat',
    'SVSFParseMask', 'DISPID_SVSpeak', 'SRARoot',
    'SpeechDataKeyLocation', 'SPCT_COMMAND', 'SP_VISEME_12',
    'SpeechCategoryPhoneConverters', 'SPSMF_SAPI_PROPERTIES',
    'SpNotifyTranslator', 'SSSPTRelativeToCurrentPosition',
    'SpSharedRecognizer', 'DISPID_SLPSymbolic', 'DISPID_SOTCId',
    'DISPID_SpeechLexiconWord', 'SSSPTRelativeToStart', 'ISpPhrase',
    'SPSModifier', 'DISPID_SPPsCount', 'SVP_15', 'eLEXTYPE_PRIVATE7',
    'SpeechTokenShellFolder', 'SPEI_SR_AUDIO_LEVEL',
    'DISPID_SpeechRecognizer', 'DISPID_SpeechPhoneConverter',
    'SPPS_SuppressWord', 'SPGS_DISABLED', 'SAFT44kHz16BitMono',
    'SVEStartInputStream', 'ISpLexicon', 'DISPID_SLWWord',
    'DISPID_SPRuleFirstElement', 'SAFT12kHz16BitStereo',
    'SPEI_REQUEST_UI', 'SGRSTTTextBuffer',
    'DISPID_SRSetPropertyNumber', 'ISpEventSink', 'SPEI_SOUND_START',
    'SPFM_OPEN_READWRITE', 'DISPID_SOTMatchesAttributes',
    'SWTDeleted', 'SDA_Consume_Leading_Spaces', 'SRTReSent',
    'DISPID_SpeechFileStream', 'SRATopLevel', 'SREStreamEnd',
    'DISPID_SMSGetData', 'DISPID_SVRate', 'ISpeechGrammarRule',
    'SpMemoryStream', 'DISPID_SLGetWords', 'DISPID_SGRAddState',
    'DISPID_SVGetAudioOutputs', 'DISPID_SOTId', 'SITooFast',
    'DISPID_SPEDisplayAttributes', 'SGRSTTWord', 'SPLO_STATIC',
    'SPSNotOverriden', 'SVSFParseAutodetect', 'SPVPRIORITY',
    'SWPUnknownWordPronounceable', 'SAFT48kHz16BitStereo',
    'SP_VISEME_2', 'SPEI_TTS_BOOKMARK', 'SPFM_NUM_MODES',
    'SGRSTTWildcard', 'SPEI_ACTIVE_CATEGORY_CHANGED',
    'DISPID_SVGetProfiles', 'SAFT24kHz16BitMono', 'SPRS_INACTIVE',
    'SLOStatic', 'SpeechVoiceSkipTypeSentence',
    'DISPID_SRRSpeakAudio', 'STCLocalServer', 'SAFT32kHz8BitMono',
    'DISPID_SRCEPropertyStringChange', 'SPEI_MIN_TTS', 'SPSNoun',
    'DISPID_SRGetPropertyString', 'SPBO_AHEAD',
    'DISPID_SpeechPhraseRules', 'SPBO_PAUSE',
    'DISPID_SLPPartOfSpeech', 'SPWORDPRONUNCIATION',
    'SECFEmulateResult', 'eLEXTYPE_PRIVATE17', 'SPRULE',
    'SPPROPERTYINFO', 'SP_VISEME_14', 'SP_VISEME_16',
    'SpeechPropertyHighConfidenceThreshold', 'SVEBookmark',
    'eLEXTYPE_VENDORLEXICON', 'eLEXTYPE_PRIVATE14',
    'ISpeechCustomStream', 'SPSERIALIZEDRESULT',
    'SpeechAudioFormatGUIDText', 'DISPID_SPRules_NewEnum',
    'SDA_One_Trailing_Space', 'SPSInterjection', 'SPRULESTATE',
    'SREAudioLevel', 'DISPID_SVEBookmark', 'SPRECOSTATE',
    'DISPID_SpeechBaseStream', 'tagSTATSTG', 'SASStop', 'SVP_3',
    'SPPS_Verb', 'eLEXTYPE_PRIVATE19', 'SAFTADPCM_22kHzMono',
    'ISpeechXMLRecoResult',
    'DISPID_SpeechGrammarRuleStateTransitions', 'SPCATEGORYTYPE',
    'ISpeechLexicon', 'SSTTDictation', 'eWORDTYPE_ADDED', 'SVP_13',
    'DISPID_SPEAudioStreamOffset', 'DISPID_SPERetainedStreamOffset',
    'SAFT48kHz8BitMono', 'SP_VISEME_5', 'SRTEmulated', 'SVF_None',
    'SPEI_UNDEFINED', 'DISPID_SRGId', 'DISPID_SAFGuid', 'SP_VISEME_7',
    'DISPID_SpeechPhraseAlternates', 'DISPID_SRCESoundEnd',
    'SpeechRuleState', 'SPAUDIOBUFFERINFO', 'SRTAutopause',
    'SRADefaultToActive', 'SPGS_ENABLED', 'SAFTGSM610_22kHzMono',
    'DISPID_SGRSTPropertyName', 'SVP_10', 'SRSActive',
    'DISPID_SGRsFindRule', 'SAFT16kHz8BitMono',
    'DISPID_SVAudioOutputStream', 'SAFTADPCM_44kHzMono',
    'SPPARTOFSPEECH', 'SPSSuppressWord', 'SpeechMicTraining',
    'DISPID_SRCVoice', 'ISpRecoGrammar', 'SRSInactiveWithPurge',
    'DISPID_SRIsShared', 'DISPID_SpeechObjectToken',
    'DISPID_SRGCmdLoadFromObject', 'DISPID_SPPName',
    'DISPID_SPRulesItem', 'DISPID_SPEs_NewEnum', 'SPLOADOPTIONS',
    'ISpProperties', 'DISPID_SpeechLexiconProns', 'SDTAlternates',
    'DISPID_SDKSetStringValue', 'DISPID_SABufferInfo',
    'DISPID_SPPValue', 'SPAR_High', 'SP_VISEME_17',
    'SVSFNLPSpeakPunc', 'DISPID_SOTCDefault', 'IEnumSpObjectTokens',
    'ISpEventSource', 'SDA_No_Trailing_Space',
    'ISpeechPhraseProperties', 'SVP_21', 'DISPID_SASetState',
    'DISPID_SWFEFormatTag', 'eWORDTYPE_DELETED',
    'DISPID_SLGetPronunciations', 'SPINTERFERENCE_TOOQUIET',
    'eLEXTYPE_RESERVED4', 'SpeechAudioVolume', 'DISPID_SRRTLength',
    'DISPID_SpeechRecoContext', 'DISPID_SDKGetBinaryValue',
    'DISPID_SLPs_NewEnum', '__MIDL___MIDL_itf_sapi_0000_0020_0002',
    'ISpeechTextSelectionInformation', 'SVSFPersistXML',
    'SSFMOpenReadWrite', 'SpResourceManager', 'SAFT8kHz16BitStereo',
    'ISpPhoneticAlphabetSelection', 'SGRSTTEpsilon', 'SRCS_Enabled',
    'SPEI_MIN_SR', 'SPSHORTCUTTYPE', 'SVP_6',
    'DISPID_SRRGetXMLResult', 'SpeechRecognitionType',
    'DISPID_SPRFirstElement', 'SDKLLocalMachine', 'DISPID_SPEsItem',
    'SpeechLoadOption', 'SRSActiveAlways', 'DISPID_SGRSTransitions',
    'eLEXTYPE_PRIVATE2', 'DISPID_SGRSRule',
    'DISPID_SPEAudioTimeOffset', 'DISPID_SOTDisplayUI',
    'DISPID_SDKCreateKey', 'SECNormalConfidence',
    'SGDSActiveUserDelimited', 'SVEViseme', 'SAFT32kHz16BitMono',
    'SGDSActiveWithAutoPause', 'DISPID_SpeechPhraseRule',
    'DISPID_SGRSTs_NewEnum', 'DISPID_SVESentenceBoundary',
    'SPEI_ADAPTATION', 'SITooSlow', 'DISPID_SVSInputSentencePosition',
    'SpCustomStream', 'ISpeechResourceLoader', 'SPAR_Unknown',
    'ISpObjectToken', 'Library', 'SRTExtendableParse',
    '_ISpeechVoiceEvents', 'DISPID_SpeechAudioStatus',
    'SAFT12kHz16BitMono', 'SAFT12kHz8BitStereo',
    'DISPID_SVSLastResult', 'SPPHRASERULE', 'SINoSignal',
    'SITooQuiet', 'eLEXTYPE_PRIVATE15', 'SP_VISEME_9',
    'SPFM_CREATE_ALWAYS', 'ISpeechLexiconWords',
    'DISPID_SpeechMemoryStream', '_RemotableHandle',
    'DISPID_SRGRules', 'SPSMF_SRGS_SEMANTICINTERPRETATION_MS',
    'DISPID_SPPChildren', 'SpPhoneticAlphabetConverter',
    'DISPID_SVEStreamEnd', 'IInternetSecurityMgrSite',
    'SVEVoiceChange', 'DISPID_SOTSetId',
    'DISPID_SVSpeakCompleteEvent', 'DISPID_SOTDataKey',
    'DISPID_SGRAttributes', 'DISPID_SRRecognizer', 'SASPause',
    'ISpNotifySource', 'DISPID_SVSkip', 'DISPID_SRStatus',
    'SAFT22kHz8BitStereo', 'ISpeechObjectToken', 'ISpPhraseAlt',
    'SPTEXTSELECTIONINFO', 'SDTAudio',
    'DISPID_SRSNumberOfActiveRules', 'SPEI_INTERFERENCE',
    'SPINTERFERENCE_TOOFAST', 'DISPID_SGRAddResource',
    'SAFT16kHz16BitMono', 'DISPID_SRGCmdLoadFromFile', 'IStream',
    'DISPID_SRCEPhraseStart', 'SPEI_SR_BOOKMARK',
    'DISPID_SpeechCustomStream', 'SVP_2', 'DISPID_SPPId',
    'DISPID_SPIElements', 'DISPID_SGRsItem',
    'DISPID_SRCEFalseRecognition', 'DISPID_SVSInputSentenceLength',
    'SPFM_OPEN_READONLY', 'SpeechWordPronounceable', 'SPWF_INPUT',
    'SAFTGSM610_44kHzMono', 'DISPID_SpeechPhraseBuilder',
    'SpeechAudioState', 'SPEI_PHONEME', 'SAFTNoAssignedFormat',
    'eLEXTYPE_USER_SHORTCUT', 'SPEVENTENUM', 'DISPID_SRRTStreamTime',
    'SP_VISEME_18', 'DISPID_SPRDisplayAttributes', 'SPAS_CLOSED',
    'DISPID_SPRuleName', 'DISPID_SLRemovePronunciationByPhoneIds',
    'DISPID_SRCEStartStream', 'DISPID_SRGCmdLoadFromMemory',
    'DISPID_SVSInputWordLength', 'SPVISEMES', 'STSF_FlagCreate',
    'DISPID_SVSCurrentStreamNumber', 'DISPID_SOTGetDescription',
    'SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN', 'DISPID_SLWsItem',
    'DISPID_SpeechGrammarRule', 'SPSEMANTICERRORINFO',
    'SAFTADPCM_8kHzMono', 'DISPID_SRGIsPronounceable',
    'DISPID_SLWPronunciations', 'eLEXTYPE_PRIVATE6',
    'DISPID_SpeechPhraseReplacements', 'SREAdaptation',
    'DISPID_SRSCurrentStreamNumber', 'DISPID_SRCPause',
    'SpeechRecognizerState', 'SRCS_Disabled', 'SPPS_Noun',
    'DISPID_SPRuleChildren', 'DISPID_SGRInitialState',
    'DISPID_SDKOpenKey', 'SAFT12kHz8BitMono',
    'DISPID_SRGetPropertyNumber', 'ISpeechGrammarRules',
    'ISpeechRecoResultTimes', 'SPEI_START_SR_STREAM',
    'DISPID_SPIStartTime', 'SpInProcRecoContext',
    'DISPID_SOTIsUISupported', 'DISPID_SVSRunningState',
    'DISPID_SLWsCount', 'SpWaveFormatEx', 'eLEXTYPE_RESERVED7',
    'SBONone', 'SSFMCreate', 'ISpRecoCategory', 'SPPHRASE',
    'SASClosed', 'DISPID_SRGReset', 'eLEXTYPE_PRIVATE4',
    'DISPID_SRCESoundStart', 'SFTInput', 'SpeechGrammarTagWildcard',
    'SpeechAudioFormatType', 'ISpeechVoiceStatus', 'SpMMAudioEnum',
    'SPSLMA', 'SPEI_END_INPUT_STREAM', 'SPAS_STOP', 'SPPS_LMA',
    'DISPID_SDKGetStringValue', 'SPCT_DICTATION', 'SPXRO_SML',
    'DISPID_SVAudioOutput', 'ISpeechAudioFormat',
    'DISPID_SRCEHypothesis', 'DISPID_SpeechPhraseElements',
    'DISPID_SDKSetLongValue', 'SREFalseRecognition',
    'SpeechCategoryRecognizers', 'DISPID_SOTCategory',
    'tagSPPROPERTYINFO', 'ISpeechBaseStream',
    'SAFTCCITT_ALaw_11kHzStereo', 'SPAS_RUN', 'SAFT24kHz16BitStereo',
    'DISPID_SVSLastStreamNumberQueued', 'SPBINARYGRAMMAR',
    'Speech_StreamPos_Asap', 'SAFTCCITT_ALaw_22kHzMono',
    'DISPID_SRCRecognizer', 'SAFT22kHz16BitStereo', 'SECFIgnoreCase',
    'eLEXTYPE_RESERVED9', 'SRSEIsSpeaking', 'SPEI_TTS_PRIVATE',
    'SAFT8kHz16BitMono', 'DISPID_SVSInputWordPosition',
    'DISPID_SRSClsidEngine', 'eLEXTYPE_PRIVATE10',
    'SpStreamFormatConverter', 'DISPID_SRCCmdMaxAlternates',
    'DISPID_SOTsItem', 'SpeechTokenKeyUI', 'SVSFIsXML',
    'DISPID_SRRTOffsetFromStart',
    'ISpeechGrammarRuleStateTransitions', 'DISPIDSPRG', 'SRAExport',
    'DISPID_SVEEnginePrivate', 'SAFTCCITT_ALaw_22kHzStereo',
    'SECFNoSpecialChars', 'ISpXMLRecoResult', 'SPXMLRESULTOPTIONS',
    'SP_VISEME_3', 'SGDisplay', 'SREAllEvents', 'SVESentenceBoundary',
    'DISPID_SRAllowAudioInputFormatChangesOnNextSet',
    'SAFT44kHz8BitStereo', 'DISPID_SPPsItem', 'SPEI_WORD_BOUNDARY',
    'eLEXTYPE_RESERVED8', 'DISPID_SRGCommit',
    'DISPID_SpeechGrammarRuleState', 'SECFIgnoreKanaType',
    'DISPID_SRRSaveToMemory', 'DISPID_SpeechPhraseReplacement',
    'DISPID_SMSALineId', 'DISPID_SPIReplacements',
    'SpeechStreamSeekPositionType', 'DISPID_SRCCreateGrammar',
    'SPRECORESULTTIMES', 'SVP_20', 'DISPID_SPRuleConfidence',
    'DISPID_SGRSTType', 'SPWT_DISPLAY', 'SPRS_ACTIVE_WITH_AUTO_PAUSE',
    'SLTApp', 'DISPID_SASCurrentDevicePosition', 'SPWT_PRONUNCIATION',
    'ISpeechPhraseReplacement', 'SPWORDPRONUNCIATIONLIST',
    'DISPID_SRRAudio', 'SpCompressedLexicon', 'SFTSREngine',
    'DISPID_SAEventHandle', 'ISpVoice', 'ISpeechRecoResultDispatch',
    'SPSHT_NotOverriden', 'SpeechGrammarState',
    '__MIDL___MIDL_itf_sapi_0000_0020_0001', 'SPEI_RESERVED3',
    'DISPID_SVEStreamStart', 'DISPID_SVSVisemeId', 'SPEI_SOUND_END',
    'ISpeechPhraseInfo', 'DISPID_SpeechDataKey', 'DISPID_SPRsCount',
    'SPSMF_UPS', 'SGSDisabled', 'DISPID_SABufferNotifySize',
    'SPWORDTYPE', 'ISpeechObjectTokens', 'SSFMCreateForWrite',
    'ISpeechRecoGrammar', 'SAFTCCITT_uLaw_22kHzMono',
    'SRERecoOtherContext', 'DISPID_SRCERecognition', 'SVP_0',
    'eLEXTYPE_PRIVATE3', 'DISPID_SpeechPhraseElement', 'ISpeechAudio',
    'DISPID_SGRClear', 'SPADAPTATIONRELEVANCE', 'ISpeechWaveFormatEx',
    'DISPID_SVEAudioLevel', 'DISPID_SpeechRecoResult',
    'DISPID_SOTCreateInstance', 'SVSFIsFilename',
    'DISPID_SVSLastBookmark', 'SAFT44kHz8BitMono',
    'Speech_Default_Weight', 'eLEXTYPE_APP', 'SpAudioFormat',
    'SPEI_MAX_TTS', 'SPPS_Modifier', 'SRTStandard', 'ISpNotifySink',
    'SpeechVoiceCategoryTTSRate', 'SAFTExtendedAudioFormat',
    'SPEVENTSOURCEINFO', 'SpeechGrammarTagDictation', 'IEnumString',
    'DISPID_SpeechVoice', 'eLEXTYPE_USER', 'SPRST_ACTIVE_ALWAYS',
    'SpObjectTokenCategory', 'ISpeechLexiconPronunciation',
    'DISPID_SASFreeBufferSpace', 'STCInprocServer',
    'DISPID_SASNonBlockingIO', 'SPINTERFERENCE_LATENCY_TRUNCATE_END',
    'SAFT16kHz8BitStereo', 'DISPID_SGRName', 'SpeechInterference',
    'DISPID_SPELexicalForm', 'SPDKL_LocalMachine', 'DISPID_SPPParent',
    'DISPID_SLWType', 'STCInprocHandler', 'SpSharedRecoContext',
    'DISPID_SpeechObjectTokens', 'SPPS_RESERVED2', 'SP_VISEME_13',
    'SPEI_RECO_STATE_CHANGE', 'DISPID_SPAs_NewEnum',
    'SPEI_TTS_AUDIO_LEVEL', 'SpPhraseInfoBuilder',
    'DISPID_SVSpeakStream', 'DISPID_SRSCurrentStreamPosition',
    'DISPID_SRDisplayUI', 'SAFT11kHz8BitMono',
    'ISpeechPhraseAlternate', 'SAFT24kHz8BitStereo',
    'DISPID_SPARecoResult', 'SPWP_UNKNOWN_WORD_PRONOUNCEABLE',
    'SRERecognition', 'ISpeechRecognizer', 'SP_VISEME_4',
    'SPFM_CREATE', 'SPSERIALIZEDPHRASE', 'SAFT11kHz16BitMono',
    'DISPID_SBSFormat', 'SpeechVoiceSpeakFlags', 'SpeechPartOfSpeech',
    'tagSPTEXTSELECTIONINFO', 'SPSHORTCUTPAIRLIST', 'SPVPRI_ALERT',
    'SpeechRecoProfileProperties', 'SPEI_RECOGNITION',
    'SWPKnownWordPronounceable', 'DISPID_SAFType', 'DISPID_SAVolume',
    'DISPID_SPIEngineId', 'DISPID_SPPFirstElement', 'SPEI_HYPOTHESIS',
    'DISPID_SVEViseme', 'SP_VISEME_21', 'SAFTCCITT_uLaw_11kHzStereo',
    'DISPID_SGRSAddWordTransition', 'DISPID_SPIRule',
    'DISPID_SVGetVoices', 'SP_VISEME_0', 'DISPID_SVWaitUntilDone',
    'SDTRule', 'SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE',
    'SpeechTokenIdUserLexicon', 'WAVEFORMATEX', 'SPVPRI_NORMAL',
    'DISPID_SRCEInterference', 'SAFTCCITT_ALaw_8kHzStereo',
    'eLEXTYPE_PRIVATE5', 'DISPID_SWFEBitsPerSample',
    'SpPhoneConverter', 'SVP_7', 'ISpRecognizer2',
    'SPINTERFERENCE_TOOSLOW', 'SPVOICESTATUS', 'eLEXTYPE_PRIVATE12',
    'SVEWordBoundary', 'DISPID_SMSSetData', 'DISPID_SRGetRecognizers',
    'SVF_Emphasis', 'DISPID_SPEPronunciation',
    'SpTextSelectionInformation', 'SPAO_NONE', 'SVSFDefault',
    'DISPID_SRRRecoContext', 'SPWT_LEXICAL_NO_SPECIAL_CHARS',
    'DISPID_SPILanguageId', 'DISPID_SPRuleId',
    'DISPID_SOTGetAttribute',
    'SpeechPropertyNormalConfidenceThreshold',
    'SpeechCategoryAudioOut', 'eLEXTYPE_PRIVATE1',
    'DISPID_SRCSetAdaptationData', 'SPPS_Noncontent',
    'SPDKL_CurrentUser', 'SAFT8kHz8BitMono', 'SPPS_RESERVED3',
    'SREPrivate', 'DISPID_SVEPhoneme', 'SPSMF_SRGS_SAPIPROPERTIES',
    'SAFTDefault', 'SAFTADPCM_8kHzStereo',
    'DISPID_SpeechRecoResultTimes', 'DISPID_SOTRemove',
    'DISPID_SVEWord', 'DISPID_SDKEnumValues', '__MIDL_IWinTypes_0009',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_W3C',
    'DISPIDSPTSI_ActiveLength', 'eLEXTYPE_RESERVED6',
    'SPEI_RESERVED2', 'DISPID_SGRSAddSpecialTransition',
    'DISPID_SGRSTRule', 'DISPID_SWFEBlockAlign', 'SDTPronunciation',
    'DISPID_SpeechPhraseAlternate', 'SPCT_SUB_COMMAND',
    'DISPID_SASState', 'SpeechEmulationCompareFlags',
    'DISPID_SLWLangId', 'DISPID_SRAudioInputStream',
    'DISPID_SGRSTsItem', 'SPAO_RETAIN_AUDIO', 'SPPS_RESERVED1',
    'DISPID_SMSAMMHandle', 'SGSExclusive',
    'DISPID_SRCVoicePurgeEvent', 'SpNullPhoneConverter',
    'ISpRecoResult', 'SAFT24kHz8BitMono', 'DISPID_SADefaultFormat',
    'SAFT11kHz16BitStereo', 'SECFDefault',
    'DISPID_SVSyncronousSpeakTimeout', 'ISpeechObjectTokenCategory',
    'DISPID_SpeechMMSysAudio', 'DISPID_SPIRetainedSizeBytes',
    'DISPID_SRCEPropertyNumberChange', 'DISPID_SVAlertBoundary',
    'SPEI_VISEME', 'ISpStream'
]

