from enum import IntFlag

import comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 as __wrapper_module__
from comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 import (
    SpeechPropertyHighConfidenceThreshold, _lcid, eLEXTYPE_PRIVATE10,
    SAFT22kHz16BitMono, SPEI_RECO_STATE_CHANGE, ISequentialStream,
    SPEI_SENTENCE_BOUNDARY, DISPID_SPRuleParent,
    SGLexicalNoSpecialChars, DISPID_SAVolume,
    IInternetSecurityManager, SWPKnownWordPronounceable,
    DISPID_SGRSAddWordTransition, DISPID_SGRSTText, SpeechAudioVolume,
    DISPID_SASFreeBufferSpace, DISPID_SLGenerationId,
    SPRECOCONTEXTSTATUS, SAFTGSM610_11kHzMono, DISPID_SRRAudio,
    DISPIDSPTSI_ActiveLength, eWORDTYPE_DELETED,
    SGDSActiveUserDelimited, DISPID_SRAudioInputStream,
    DISPID_SRProfile, SAFT12kHz8BitMono, _FILETIME, SPAS_RUN,
    DISPID_SGRSRule, Library, SPAO_RETAIN_AUDIO, SPWT_PRONUNCIATION,
    SPWF_SRENGINE, SDKLCurrentUser, SAFTCCITT_ALaw_11kHzMono,
    SGDSActive, SPGS_ENABLED, SPRECOGNIZERSTATUS, SPRULE,
    DISPID_SBSWrite, DISPID_SWFEChannels, ISpeechPhraseAlternate,
    DISPID_SPRulesItem, ISpGrammarBuilder, SPGS_DISABLED,
    ISpObjectTokenCategory, ISpPhrase,
    DISPID_SLRemovePronunciationByPhoneIds, DISPID_SRGIsPronounceable,
    SAFT24kHz16BitStereo, SAFTCCITT_uLaw_22kHzMono, SP_VISEME_15,
    SAFT22kHz16BitStereo, DISPID_SRIsShared,
    DISPID_SPEActualConfidence, DISPID_SRGetFormat, SP_VISEME_13,
    SVP_14, DISPID_SRRAudioFormat,
    SpeechPropertyLowConfidenceThreshold, SVP_17, SVP_12, SDTRule,
    SPEI_TTS_BOOKMARK, SRATopLevel, SAFT8kHz16BitStereo,
    DISPID_SGRsCommit, SAFT12kHz8BitStereo, SECHighConfidence,
    ISpeechPhraseReplacement, DISPID_SGRSAddSpecialTransition,
    DISPID_SRRSetTextFeedback, SVPAlert, SREStreamEnd,
    SPRECORESULTTIMES, SPVPRI_NORMAL, DISPID_SASetState,
    ISpeechPhraseRule, ISpRecoContext, DISPID_SOTCGetDataKey,
    SRTSMLTimeout, SRESoundStart, DISPID_SPEDisplayText,
    DISPID_SPIEnginePrivateData, SP_VISEME_19, SPRST_ACTIVE_ALWAYS,
    SpeechAudioProperties, Speech_Max_Word_Length,
    SAFTCCITT_ALaw_44kHzMono, SpStreamFormatConverter, SPCT_DICTATION,
    SVSFVoiceMask, SPWF_INPUT, SpPhoneticAlphabetConverter,
    DISPID_SGRSAddRuleTransition, DISPID_SVSLastBookmarkId,
    SpeechPropertyNormalConfidenceThreshold, SPEI_SR_PRIVATE,
    DISPID_SOTGetDescription, Speech_Default_Weight,
    DISPID_SDKEnumValues, DISPID_SVSyncronousSpeakTimeout, SVP_8,
    SPRST_INACTIVE_WITH_PURGE, SRAImport, SP_VISEME_21, SVP_16,
    DISPID_SVSpeakStream, SECFIgnoreKanaType, SRSInactiveWithPurge,
    SVSFIsNotXML, DISPID_SRGCmdLoadFromFile, ISpeechGrammarRuleState,
    SPFM_NUM_MODES, SDTAlternates, eLEXTYPE_RESERVED6,
    DISPID_SRCState, SpCompressedLexicon, SpeechCategoryAppLexicons,
    SPAS_CLOSED, DISPID_SOTIsUISupported, SAFT8kHz8BitMono,
    IEnumSpObjectTokens, SVP_3, SPRS_ACTIVE_USER_DELIMITED, SPAO_NONE,
    DISPID_SPIGetText, _ISpeechRecoContextEvents, SVP_7,
    SPPHRASEPROPERTY, SpeechTokenKeyFiles, dispid, SPEI_VISEME,
    SREFalseRecognition, DISPID_SPCLangId, DISPID_SASNonBlockingIO,
    SPLO_DYNAMIC, DISPID_SGRSTNextState, ISpeechPhraseRules,
    DISPID_SPELexicalForm, DISPID_SPEEngineConfidence,
    SpeechGrammarTagWildcard, SRTStandard, DISPID_SGRs_NewEnum,
    wireHWND, _LARGE_INTEGER, SAFT8kHz16BitMono, SP_VISEME_8,
    SPEI_FALSE_RECOGNITION, SVP_4, DISPID_SVSLastBookmark,
    DISPID_SPCPhoneToId, SVF_Stressed, DISPID_SPILanguageId,
    SREBookmark, DISPID_SLPsItem, DISPID_SLWs_NewEnum, SPBO_AHEAD,
    eLEXTYPE_PRIVATE11, SPINTERFERENCE_LATENCY_WARNING,
    SpeechDictationTopicSpelling, DISPID_SPPChildren, SREStateChange,
    SPWT_LEXICAL, SPSMF_SRGS_SAPIPROPERTIES, SAFTDefault,
    DISPID_SDKGetBinaryValue, SAFTGSM610_44kHzMono,
    DISPID_SABufferNotifySize, DISPID_SRGCmdLoadFromMemory, SRAONone,
    SPSVerb, DISPID_SDKCreateKey, SWTAdded, ISpeechRecoContext,
    ISpeechVoiceStatus, SPRST_ACTIVE, DISPID_SOTsItem,
    SECFIgnoreWidth, DISPID_SABIMinNotification,
    SAFTCCITT_uLaw_11kHzMono, SREAllEvents, SSFMOpenReadWrite,
    DISPID_SRCEAdaptation, DISPID_SOTs_NewEnum,
    DISPID_SVWaitUntilDone, SVP_15, DISPID_SRSCurrentStreamNumber,
    SREAudioLevel, DISPID_SVEventInterests,
    DISPID_SRCEPropertyStringChange, DISPID_SCSBaseStream,
    SPEI_UNDEFINED, DISPID_SOTCId, DISPID_SVSInputWordPosition,
    ISpeechTextSelectionInformation, SVEPrivate,
    SWPUnknownWordPronounceable, DISPID_SPIEngineId,
    DISPID_SRCCreateResultFromMemory, SITooSlow,
    SPINTERFERENCE_TOOFAST, SPEI_RESERVED1,
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS, SAFT44kHz16BitMono,
    Speech_StreamPos_RealTime, SRERequestUI, STSF_LocalAppData,
    SPEI_ADAPTATION, SP_VISEME_10, SAFT12kHz16BitStereo,
    ISpNotifySource, DISPID_SOTMatchesAttributes, SAFTADPCM_8kHzMono,
    DISPID_SRGSetTextSelection, SAFTNonStandardFormat,
    DISPID_SRRDiscardResultInfo, SPRS_ACTIVE_WITH_AUTO_PAUSE,
    SAFT24kHz8BitStereo, DISPID_SPEAudioStreamOffset,
    SAFT24kHz16BitMono, DISPID_SDKEnumKeys, eLEXTYPE_PRIVATE2,
    DISPID_SVSRunningState, DISPID_SRCAudioInInterferenceStatus,
    DISPID_SPPBRestorePhraseFromMemory, DISPID_SVEPhoneme,
    ISpSerializeState, DISPID_SWFEExtraData, SpCustomStream, SVP_9,
    tagSPPROPERTYINFO, ISpStreamFormat, ISpeechAudio,
    DISPID_SMSAMMHandle, SPSHT_NotOverriden,
    SSSPTRelativeToCurrentPosition, DISPID_SDKDeleteKey,
    DISPID_SASCurrentSeekPosition, DISPID_SAStatus, SPEI_MIN_TTS,
    DISPID_SPRFirstElement, DISPID_SVEWord, SVP_10, SpWaveFormatEx,
    DISPID_SVESentenceBoundary, SPPS_RESERVED4, SPRST_INACTIVE,
    eLEXTYPE_PRIVATE14, SDKLLocalMachine,
    DISPID_SPIAudioStreamPosition, ISpRecoGrammar, SpMMAudioEnum,
    DISPID_SAFGetWaveFormatEx, DISPID_SPRs_NewEnum, SPPS_RESERVED1,
    ISpeechLexiconWords, SDA_No_Trailing_Space, SPCT_SUB_COMMAND,
    DISPID_SPRules_NewEnum, DISPID_SRRTimes, SSTTDictation,
    SAFTCCITT_uLaw_11kHzStereo, SECLowConfidence, SPPS_Unknown,
    SPEI_ACTIVE_CATEGORY_CHANGED, DISPID_SPIStartTime, SREPhraseStart,
    SVSFPurgeBeforeSpeak, SAFTADPCM_44kHzMono, ISpeechWaveFormatEx,
    SAFT32kHz8BitStereo, DISPID_SRGCmdLoadFromProprietaryGrammar,
    SVEBookmark, ISpRecoCategory, SVP_1, DISPID_SRRTOffsetFromStart,
    tagSTATSTG, DISPID_SVSVisemeId, LONG_PTR, SRAInterpreter, SVP_11,
    SpeechTokenValueCLSID, DISPID_SLAddPronunciation, SpMemoryStream,
    DISPID_SVSpeakCompleteEvent, SPPS_Function, SASClosed,
    ISpeechAudioFormat, DISPID_SVRate, DISPID_SRCRecognizer,
    SPEI_END_SR_STREAM, SGSDisabled, _RemotableHandle,
    DISPIDSPTSI_SelectionLength, SPEI_HYPOTHESIS, DISPID_SGRsItem,
    ISpeechRecoGrammar, DISPID_SRCERecognitionForOtherContext,
    SPBO_TIME_UNITS, SAFT44kHz8BitMono, SVEStartInputStream,
    SpSharedRecognizer, DISPID_SOTDisplayUI, SINone,
    ISpPhoneticAlphabetSelection, SPAUDIOBUFFERINFO,
    DISPID_SRCEStartStream, DISPID_SOTCEnumerateTokens,
    DISPID_SRCERecognition, SPGS_EXCLUSIVE, SDTProperty,
    DISPID_SLGetPronunciations, DISPID_SRCRetainedAudio,
    DISPID_SVSLastStreamNumberQueued, eLEXTYPE_PRIVATE18,
    WAVEFORMATEX, DISPID_SPIElements, SVSFUnusedFlags, SDTAudio,
    SAFTCCITT_uLaw_8kHzMono, SPDKL_CurrentUser,
    DISPID_SLPPartOfSpeech, SAFTCCITT_ALaw_22kHzStereo,
    SPEI_REQUEST_UI, ISpProperties, eLEXTYPE_PRIVATE9,
    eLEXTYPE_PRIVATE12, SPPS_RESERVED2, SPWORDLIST,
    DISPID_SRGCmdSetRuleState, DISPID_SVGetAudioOutputs, IEnumString,
    eLEXTYPE_USER_SHORTCUT, DISPID_SGRAddState,
    SpeechAudioFormatGUIDText, SpInprocRecognizer, SRCS_Enabled,
    ISpDataKey, DISPID_SOTGetStorageFileName, SPINTERFERENCE_TOOSLOW,
    ISpeechPhraseInfo, DISPID_SPPName, SpeechCategoryPhoneConverters,
    SAFT22kHz8BitStereo, DISPID_SVSInputSentenceLength,
    SpTextSelectionInformation, DISPID_SRCEFalseRecognition,
    DISPID_SVIsUISupported, DISPID_SVSInputWordLength, ISpShortcut,
    SPWP_KNOWN_WORD_PRONOUNCEABLE, SAFT44kHz8BitStereo,
    DISPID_SRSClsidEngine, DISPID_SPEsCount, DISPID_SMSADeviceId,
    DISPID_SPPId, UINT_PTR, STSF_FlagCreate, SPEI_RESERVED6,
    DISPID_SWFEBitsPerSample, SpLexicon, SpSharedRecoContext,
    SPEI_PHONEME, COMMETHOD, DISPID_SAFSetWaveFormatEx, GUID,
    ISpeechLexiconPronunciations, SAFTGSM610_22kHzMono,
    DISPID_SAFType, DISPID_SVPause, eLEXTYPE_PRIVATE1,
    DISPID_SVEVoiceChange, __MIDL_IWinTypes_0009,
    SpeechGrammarTagUnlimitedDictation, ISpeechMMSysAudio,
    STCInprocServer, SPWORDPRONUNCIATION, ISpeechPhraseAlternates,
    DISPID_SRGId, DISPIDSPTSI_SelectionOffset, SpResourceManager,
    DISPID_SLPsCount, tagSPTEXTSELECTIONINFO, SPSHT_EMAIL,
    SAFT32kHz16BitMono, SpeechCategoryAudioIn,
    DISPID_SRAllowAudioInputFormatChangesOnNextSet,
    DISPID_SGRsCommitAndSave, DISPID_SLPs_NewEnum, SGDisplay,
    SPSHT_Unknown, SPEI_PROPERTY_STRING_CHANGE, SRTExtendableParse,
    SAFT48kHz8BitStereo, SP_VISEME_11, SVF_Emphasis,
    DISPID_SPEs_NewEnum, SPPS_SuppressWord, SPRS_ACTIVE, SPAS_STOP,
    ISpeechXMLRecoResult, DISPID_SRGReset, SVPNormal, eWORDTYPE_ADDED,
    SPEI_SR_BOOKMARK, DISPID_SPERequiredConfidence,
    __MIDL___MIDL_itf_sapi_0000_0020_0001, DISPID_SPRsItem,
    DISPID_SPPValue, SVP_6, SAFT16kHz16BitMono, ISpeechRecognizer,
    DISPID_SRSetPropertyString, DISPID_SPPs_NewEnum,
    SpNotifyTranslator, SRSEDone, DISPID_SRRTStreamTime,
    ISpeechObjectTokenCategory, SpeechCategoryRecoProfiles,
    SAFTADPCM_22kHzStereo, SAFTADPCM_11kHzMono, DISPID_SPCIdToPhone,
    Speech_Max_Pron_Length, SDTAll, DISPID_SMSGetData,
    SpeechEngineProperties, SDA_Consume_Leading_Spaces,
    DISPID_SGRSTs_NewEnum, eLEXTYPE_PRIVATE19, DISPID_SGRSTsItem,
    SPAS_PAUSE, SREAdaptation, eLEXTYPE_RESERVED8, SVSFDefault,
    SGDSInactive, DISPID_SASCurrentDevicePosition, SP_VISEME_17,
    SRTEmulated, SRERecoOtherContext, SPEI_MAX_SR, ISpeechLexiconWord,
    DISPID_SRIsUISupported, SAFT16kHz16BitStereo, SVSFIsFilename,
    ISpRecoGrammar2, _ISpeechVoiceEvents, DISPID_SRCEPhraseStart,
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C, ISpStream, SPAUDIOSTATUS,
    SPINTERFERENCE_NOISE, SPWT_DISPLAY, SPSSuppressWord, SLTApp,
    DISPID_SRRGetXMLErrorInfo, DISPID_SPIRetainedSizeBytes,
    ISpeechMemoryStream, SAFTADPCM_22kHzMono, ISpRecognizer,
    SpAudioFormat, STCLocalServer, SECFEmulateResult,
    DISPID_SGRSTPropertyId, DISPID_SLGetWords, DISPID_SOTCDefault,
    SP_VISEME_0, SRADynamic, DISPID_SPIAudioSizeTime,
    DISPID_SLRemovePronunciation, DISPID_SDKOpenKey,
    SAFT48kHz16BitStereo, eLEXTYPE_MORPHOLOGY, DISPID_SVDisplayUI,
    DISPID_SPPEngineConfidence, SPWORDPRONUNCIATIONLIST,
    DISPID_SGRSTType, ISpeechVoice, SP_VISEME_16,
    SPEI_START_INPUT_STREAM, DISPID_SOTSetId, SPSHORTCUTPAIRLIST,
    SVP_18, DISPID_SOTCSetId, DISPID_SMSSetData,
    SPINTERFERENCE_LATENCY_TRUNCATE_END, DISPID_SVGetProfiles,
    DISPID_SVAudioOutputStream, SGRSTTDictation,
    DISPID_SRSAudioStatus, SPPS_LMA, SP_VISEME_7, DISPID_SAFGuid,
    DISPID_SRCVoice, ISpeechRecognizerStatus, SVEViseme, ISpPhraseAlt,
    SDTDisplayText, ISpeechGrammarRuleStateTransitions,
    SpeechPropertyComplexResponseSpeed, DISPID_SRCCreateGrammar,
    DISPID_SDKSetStringValue, DISPID_SRCEPropertyNumberChange,
    DISPID_SRGSetWordSequenceData, SPEVENT, DISPID_SDKGetlongValue,
    DISPID_SVSInputSentencePosition, DISPID_SVAudioOutput,
    SSSPTRelativeToEnd, DISPID_SPARecoResult, SPSNoun,
    DISPID_SGRsDynamic, SPSERIALIZEDRESULT, ISpeechPhraseReplacements,
    DISPID_SPRuleNumberOfElements, SREPropertyStringChange,
    SPINTERFERENCE_NOSIGNAL, DISPID_SVSLastResult,
    DISPID_SRGetRecognizers, DISPID_SRGCmdSetRuleIdState,
    ISpeechPhraseInfoBuilder, SPAR_High, DISPID_SGRsFindRule,
    DISPID_SPERetainedSizeBytes, SPDKL_CurrentConfig,
    SpeechTokenKeyAttributes, SPRST_NUM_STATES, SP_VISEME_4,
    SSFMCreate, DISPID_SRRPhraseInfo, DISPID_SOTGetAttribute,
    SDKLCurrentConfig, SPEI_MAX_TTS, eLEXTYPE_PRIVATE6,
    SPEI_SR_AUDIO_LEVEL, SVP_2, DISPID_SRRAlternates, SDTLexicalForm,
    SPWORD, SPFM_OPEN_READWRITE, ISpLexicon, SVSFPersistXML,
    DISPID_SFSOpen, DISPID_SLPType, eLEXTYPE_PRIVATE3,
    DISPID_SRCCmdMaxAlternates, DISPID_SPACommit, SPEVENTSOURCEINFO,
    SAFT11kHz8BitMono, SAFTText, ISpXMLRecoResult, DISPID_SVStatus,
    SpeechVoiceSkipTypeSentence, DISPID_SRCERequestUI, SRSEIsSpeaking,
    Speech_StreamPos_Asap, SGRSTTTextBuffer, DISPID_SAEventHandle,
    DISPID_SRSetPropertyNumber, SRESoundEnd, SDTReplacement,
    DISPID_SRGCmdLoadFromResource, DISPID_SPEPronunciation,
    ISpeechGrammarRuleStateTransition, ISpeechPhraseElement,
    DISPID_SRGCommit, DISPID_SDKSetLongValue, ISpeechLexicon,
    SVEWordBoundary, __MIDL___MIDL_itf_sapi_0000_0020_0002, SPBO_NONE,
    SVF_None, SGRSTTRule, eLEXTYPE_PRIVATE13, SPEI_TTS_AUDIO_LEVEL,
    SVSFParseAutodetect, SAFTNoAssignedFormat, ISpEventSource,
    DISPID_SPIRule, DISPID_SVGetAudioInputs, SDKLDefaultLocation,
    SAFT11kHz16BitMono, DISPID_SRCEventInterests, STSF_CommonAppData,
    SP_VISEME_6, SGSExclusive, DISPID_SRRSaveToMemory,
    DISPID_SWFESamplesPerSec,
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet, DISPID_SGRName,
    SVP_21, SAFTCCITT_uLaw_22kHzStereo, SPAR_Unknown,
    SPXRO_Alternates_SML, eLEXTYPE_PRIVATE16, DISPID_SPAsItem,
    DISPID_SLWsItem, SRSInactive, DISPID_SPISaveToMemory,
    SPEI_PROPERTY_NUM_CHANGE, DISPID_SGRSTransitions, SVEAudioLevel,
    SVP_5, SAFTCCITT_ALaw_22kHzMono, DISPID_SOTRemoveStorageFileName,
    ISpObjectWithToken, DISPID_SRStatus, ISpeechRecoResultTimes,
    DISPID_SPPParent, SVSFNLPMask, SPDKL_DefaultLocation,
    SpInProcRecoContext, SP_VISEME_5, SpeechUserTraining,
    DISPID_SRCRequestedUIType, DISPID_SPRuleConfidence,
    SpeechPropertyResourceUsage, DISPIDSPTSI_ActiveOffset,
    DISPID_SVSpeak, SRAExport, SECFDefault, SDA_One_Trailing_Space,
    SPSMF_SAPI_PROPERTIES, DISPID_SRState, DISPID_SGRSTRule,
    SGRSTTWord, SpeechCategoryVoices, SpeechCategoryRecognizers,
    SpUnCompressedLexicon, SINoise, DISPID_SOTCategory,
    ISpNotifyTranslator, DISPID_SADefaultFormat, eLEXTYPE_APP,
    DISPID_SRRGetXMLResult, DISPID_SLAddPronunciationByPhoneIds,
    SPINTERFERENCE_NONE, DISPID_SVPriority, SPEI_MIN_SR,
    DISPID_SPRuleFirstElement, DISPID_SPAPhraseInfo, DISPID_SVResume,
    SSTTWildcard, SPPROPERTYINFO, SAFTCCITT_uLaw_44kHzStereo,
    ISpPhoneticAlphabetConverter, SREInterference,
    eLEXTYPE_LETTERTOSOUND, SPWP_UNKNOWN_WORD_PRONOUNCEABLE,
    ISpeechPhraseElements, SAFTTrueSpeech_8kHz1BitMono,
    SAFTCCITT_uLaw_44kHzMono, SRADefaultToActive, DISPID_SLPSymbolic,
    SPFM_CREATE_ALWAYS, SAFTCCITT_ALaw_11kHzStereo, ISpRecognizer3,
    SREPrivate, DISPID_SDKSetBinaryValue, IServiceProvider,
    SAFTGSM610_8kHzMono, DISPID_SRSSupportedLanguages,
    eLEXTYPE_PRIVATE20, DISPID_SPRDisplayAttributes,
    eLEXTYPE_PRIVATE7, SpeechTokenKeyUI, ISpPhoneConverter,
    SPLO_STATIC, DISPID_SPERetainedStreamOffset, SPEI_RESERVED5,
    DISPID_SLWType, SPBINARYGRAMMAR, SAFT8kHz8BitStereo,
    ISpeechPhraseProperties, IInternetSecurityMgrSite,
    DISPID_SVEStreamStart, DISPID_SRCEBookmark, DISPID_SGRsCount,
    DISPID_SVSCurrentStreamNumber, DISPID_SVEAudioLevel, SP_VISEME_1,
    SAFT11kHz8BitStereo, ISpeechLexiconPronunciation,
    DISPID_SRCBookmark, DISPID_SOTRemove, SVSFNLPSpeakPunc,
    DISPID_SPRNumberOfElements, DISPID_SVEBookmark, SPSMF_UPS, SPSLMA,
    DISPID_SRCEHypothesis, DISPID_SPPsCount,
    DISPID_SRGetPropertyString, SAFTCCITT_ALaw_8kHzMono,
    DISPID_SPRuleChildren, SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE,
    SVSFIsXML, DISPID_SWFEFormatTag, SAFT16kHz8BitMono,
    SAFT44kHz16BitStereo, SPSFunction, SpeechPropertyResponseSpeed,
    DISPID_SRDisplayUI, DISPID_SREmulateRecognition,
    DISPID_SRGetPropertyNumber, SECFIgnoreCase, STCInprocHandler,
    SVPOver, ISpResourceManager, ISpEventSink, SWTDeleted, SPSUnknown,
    eLEXTYPE_RESERVED10, SVEVoiceChange, SPPS_Verb, DISPID_SRGState,
    SPPS_Modifier, DISPID_SLWsCount, DISPID_SDKDeleteValue, SITooLoud,
    SVEEndInputStream, _ULARGE_INTEGER, ISpeechResourceLoader,
    DISPID_SGRClear, SPPHRASE, ISpRecognizer2,
    DISPID_SPEAudioSizeTime, SpeechPropertyAdaptationOn, SASPause,
    SRERecognition, SPEI_SOUND_END, DISPID_SRSCurrentStreamPosition,
    DISPID_SPAsCount, DISPID_SLGetGenerationChange, _check_version,
    DISPID_SRGRecoContext, DISPID_SPRuleName, DISPID_SPIReplacements,
    DISPID_SFSClose, SPFM_OPEN_READONLY, SAFTCCITT_ALaw_8kHzStereo,
    SPEI_VOICE_CHANGE, SAFT12kHz16BitMono, helpstring,
    DISPID_SRCVoicePurgeEvent, SASStop, SPAR_Low, SPCT_SLEEP,
    SPEI_TTS_PRIVATE, DISPID_SPRText, DISPID_SPRuleId, SPXRO_SML,
    SAFT32kHz16BitStereo, ISpRecoContext2, SVP_19,
    SpeechTokenIdUserLexicon, DISPID_SVVoice, SLOStatic,
    SpeechCategoryAudioOut, SPINTERFERENCE_TOOLOUD, SP_VISEME_18,
    SVEPhoneme, ISpRecoResult, ISpeechGrammarRule, SGPronounciation,
    SGLexical, SVSFlagsAsync, SAFT32kHz8BitMono, SPEI_RESERVED3,
    ISpeechRecoResultDispatch, DISPID_SPEsItem, typelib_path,
    DISPID_SRRTTickCount, SFTInput, STSF_AppData, ISpeechObjectTokens,
    SP_VISEME_20, SPEI_RESERVED2, IStream, SVP_0, DISPID_SOTId,
    SpFileStream, SSFMOpenForRead, CoClass, SP_VISEME_12,
    DISPID_SPRulesCount, SPTEXTSELECTIONINFO, SpVoice,
    eLEXTYPE_PRIVATE5, SAFT22kHz8BitMono, ISpObjectToken,
    SPWT_LEXICAL_NO_SPECIAL_CHARS, HRESULT, SRTReSent, SGRSTTEpsilon,
    DISPID_SLWLangId, SPEI_START_SR_STREAM, DISPID_SRRRecoContext,
    DISPID_SBSFormat, SAFTADPCM_44kHzStereo,
    DISPID_SRGCmdLoadFromObject, SpeechAllElements,
    SpeechAddRemoveWord, SPRS_INACTIVE, SPBO_PAUSE,
    ISpeechGrammarRules, DISPID_SABIEventBias, eLEXTYPE_PRIVATE17,
    DISPID_SGRAddResource, DISPID_SRGDictationLoad, SITooFast,
    SPEI_RECOGNITION, SGRSTTWildcard, SPCT_COMMAND, DISPID_SPPsItem,
    SRSActive, DISPID_SVEViseme, DISPID_SRCEEndStream,
    DISPID_SRCESoundStart, ISpeechRecoResult, SpeechRegistryUserRoot,
    SECFNoSpecialChars, SPEI_RECO_OTHER_CONTEXT,
    DISPID_SWFEBlockAlign, SWPUnknownWordUnpronounceable,
    DISPID_SGRId, DISPID_SDKGetStringValue, SAFT24kHz8BitMono,
    SpObjectTokenCategory, SAFTADPCM_11kHzStereo, SGSEnabled,
    SDTPronunciation, SRCS_Disabled, ISpVoice, eLEXTYPE_RESERVED9,
    DISPID_SRCESoundEnd, DISPID_SGRsAdd, eLEXTYPE_PRIVATE15,
    DISPID_SBSSeek, SpeechVoiceCategoryTTSRate, DISPID_SVGetVoices,
    DISPID_SVSPhonemeId, DISPID_SRCSetAdaptationData,
    SAFT16kHz8BitStereo, DISPID_SPEDisplayAttributes,
    ISpeechRecoResult2, DISPID_SRRTLength, DISPID_SPIProperties,
    SDA_Two_Trailing_Spaces, SPPHRASERULE, DISPID_SMSALineId,
    SPPHRASEELEMENT, DISPID_SABIBufferSize, SPPS_NotOverriden,
    DISPID_SLWPronunciations, SPVPRI_ALERT, SSTTTextBuffer, SBOPause,
    ISpStreamFormatConverter,
    DISPID_SRAllowVoiceFormatMatchingOnNextSet, ISpeechAudioStatus,
    SPSModifier, SLTUser, DISPID_SVSkip, DISPID_SLPPhoneIds,
    DISPID_SRRecognizer, DISPID_SWFEAvgBytesPerSec,
    SAFTCCITT_uLaw_8kHzStereo, SPSHT_OTHER, SPSERIALIZEDPHRASE,
    SVESentenceBoundary, SPVPRI_OVER, DISPID_SOTsCount, SpMMAudioIn,
    DISPID_SRCEEnginePrivate, SPEI_INTERFERENCE, SPEI_PHRASE_START,
    SpObjectToken, DISPID_SRAudioInput, ISpeechBaseStream, ULONG_PTR,
    DISPID_SGRSTWeight, SITooQuiet, eLEXTYPE_PRIVATE8,
    DISPID_SRSNumberOfActiveRules, SLODynamic, SECNormalConfidence,
    SINoSignal, BSTR, DISPID_SPIAudioSizeBytes, SP_VISEME_14, STCAll,
    SPEI_END_INPUT_STREAM, DISPID_SBSRead,
    DISPID_SPRuleEngineConfidence, eLEXTYPE_PRIVATE4,
    DISPID_SPPFirstElement, DISPID_SRCPause, SP_VISEME_9,
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN, eLEXTYPE_VENDORLEXICON,
    STCRemoteServer, SAFT11kHz16BitStereo, SPAR_Medium,
    ISpeechFileStream, DISPID_SOTCreateInstance, SPSEMANTICERRORINFO,
    DISPID_SRRSpeakAudio, DISPID_SPAs_NewEnum, SVEAllEvents,
    ISpMMSysAudio, DISPID_SGRAttributes, SRSActiveAlways,
    DISPID_SVEEnginePrivate, DISPID_SRCERecognizerStateChange,
    DISPID_SGRInitialState, ISpeechAudioBufferInfo,
    SpeechGrammarTagDictation, SVSFParseSsml, eLEXTYPE_USER,
    ISpeechDataKey, DISPID_SRCRetainedAudioFormat,
    DISPID_SRGDictationUnload, WSTRING, SRTAutopause,
    SpeechRecoProfileProperties, DISPID_SRCreateRecoContext, ISpAudio,
    DISPID_SRCEInterference, DISPID_SRGRules, SREStreamStart,
    SPPS_Noncontent, SFTSREngine, SSFMCreateForWrite,
    DISPID_SRCEAudioLevel, SpeechAudioFormatGUIDWave,
    DISPID_SGRSTPropertyName, SPEI_SOUND_START,
    DISPID_SPIGetDisplayAttributes, SREPropertyNumChange,
    DISPID_SPRsCount, SpStream, DISPID_SLPLangId, SRARoot,
    SAFT48kHz16BitMono, SAFTExtendedAudioFormat, SBONone,
    SVSFParseSapi, SREHypothesis, SPSNotOverriden,
    DISPID_SABufferInfo, SpPhraseInfoBuilder, SPPS_Noun,
    SPSHORTCUTPAIR, SPSInterjection, DISPID_SGRSTsCount,
    ISpeechPhoneConverter, SP_VISEME_3, DISPID_SPEAudioSizeBytes,
    SpPhoneConverter, ISpeechObjectToken, DISPID_SPIGrammarId,
    DISPID_SGRSTPropertyValue, DISPID_SVAlertBoundary,
    SSSPTRelativeToStart, SVSFParseMask, SpeechMicTraining,
    VARIANT_BOOL, SPPS_Interjection, SVP_13, DISPID_SRCResume,
    DISPID_SPEAudioTimeOffset, DISPID_SPAStartElementInResult,
    ISpeechPhraseProperty, DISPID_SRGDictationSetState, VARIANT,
    SASRun, SPEI_WORD_BOUNDARY, DISPID_SPPConfidence, SPFM_CREATE,
    SPINTERFERENCE_TOOQUIET, SGDSActiveWithAutoPause,
    SPCT_SUB_DICTATION, eLEXTYPE_RESERVED7, SP_VISEME_2, DISPMETHOD,
    SPCS_DISABLED, DISPID_SASState, DISPID_SLWWord, IUnknown,
    SAFT48kHz8BitMono, SPDKL_LocalMachine, DISPID_SPPNumberOfElements,
    ISpeechCustomStream, SAFTCCITT_ALaw_44kHzStereo, SVP_20,
    DISPID_SOTDataKey, SpMMAudioOut, SpNullPhoneConverter,
    DISPID_SVVolume, SPCS_ENABLED, SPPS_RESERVED3, ISpNotifySink,
    SPPHRASEREPLACEMENT, DISPID_SPANumberOfElementsInResult,
    eLEXTYPE_RESERVED4, SAFTADPCM_8kHzStereo,
    SpeechRegistryLocalMachineRoot, SPVOICESTATUS,
    SPEI_SR_RETAINEDAUDIO, DISPID_SVEStreamEnd, SpShortcut,
    SRAORetainAudio
)


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


class SpeechVisemeFeature(IntFlag):
    SVF_None = 0
    SVF_Stressed = 1
    SVF_Emphasis = 2


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


class SpeechBookmarkOptions(IntFlag):
    SBONone = 0
    SBOPause = 1


class SpeechRecognitionType(IntFlag):
    SRTStandard = 0
    SRTAutopause = 1
    SRTEmulated = 2
    SRTSMLTimeout = 4
    SRTExtendableParse = 8
    SRTReSent = 16


class SpeechInterference(IntFlag):
    SINone = 0
    SINoise = 1
    SINoSignal = 2
    SITooLoud = 3
    SITooQuiet = 4
    SITooFast = 5
    SITooSlow = 6


class SpeechRecognizerState(IntFlag):
    SRSInactive = 0
    SRSActive = 1
    SRSActiveAlways = 2
    SRSInactiveWithPurge = 3


class SpeechRuleAttributes(IntFlag):
    SRATopLevel = 1
    SRADefaultToActive = 2
    SRAExport = 4
    SRAImport = 8
    SRAInterpreter = 16
    SRADynamic = 32
    SRARoot = 64


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


class SpeechEngineConfidence(IntFlag):
    SECLowConfidence = -1
    SECNormalConfidence = 0
    SECHighConfidence = 1


class SPDATAKEYLOCATION(IntFlag):
    SPDKL_DefaultLocation = 0
    SPDKL_CurrentUser = 1
    SPDKL_LocalMachine = 2
    SPDKL_CurrentConfig = 5


class SpeechFormatType(IntFlag):
    SFTInput = 0
    SFTSREngine = 1


class SPVPRIORITY(IntFlag):
    SPVPRI_NORMAL = 0
    SPVPRI_ALERT = 1
    SPVPRI_OVER = 2


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


class DISPID_SpeechObjectTokens(IntFlag):
    DISPID_SOTsCount = 1
    DISPID_SOTsItem = 0
    DISPID_SOTs_NewEnum = -4


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


class SpeechGrammarWordType(IntFlag):
    SGDisplay = 0
    SGLexical = 1
    SGPronounciation = 2
    SGLexicalNoSpecialChars = 3


class SpeechSpecialTransitionType(IntFlag):
    SSTTWildcard = 1
    SSTTDictation = 2
    SSTTTextBuffer = 3


class DISPID_SpeechObjectTokenCategory(IntFlag):
    DISPID_SOTCId = 1
    DISPID_SOTCDefault = 2
    DISPID_SOTCSetId = 3
    DISPID_SOTCGetDataKey = 4
    DISPID_SOTCEnumerateTokens = 5


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


class DISPID_SpeechAudioFormat(IntFlag):
    DISPID_SAFType = 1
    DISPID_SAFGuid = 2
    DISPID_SAFGetWaveFormatEx = 3
    DISPID_SAFSetWaveFormatEx = 4


class DISPID_SpeechPhraseElements(IntFlag):
    DISPID_SPEsCount = 1
    DISPID_SPEsItem = 0
    DISPID_SPEs_NewEnum = -4


class DISPID_SpeechBaseStream(IntFlag):
    DISPID_SBSFormat = 1
    DISPID_SBSRead = 2
    DISPID_SBSWrite = 3
    DISPID_SBSSeek = 4


class DISPID_SpeechPhraseReplacement(IntFlag):
    DISPID_SPRDisplayAttributes = 1
    DISPID_SPRText = 2
    DISPID_SPRFirstElement = 3
    DISPID_SPRNumberOfElements = 4


class DISPID_SpeechAudio(IntFlag):
    DISPID_SAStatus = 200
    DISPID_SABufferInfo = 201
    DISPID_SADefaultFormat = 202
    DISPID_SAVolume = 203
    DISPID_SABufferNotifySize = 204
    DISPID_SAEventHandle = 205
    DISPID_SASetState = 206


class _SPAUDIOSTATE(IntFlag):
    SPAS_CLOSED = 0
    SPAS_STOP = 1
    SPAS_PAUSE = 2
    SPAS_RUN = 3


class DISPID_SpeechPhraseReplacements(IntFlag):
    DISPID_SPRsCount = 1
    DISPID_SPRsItem = 0
    DISPID_SPRs_NewEnum = -4


class SpeechGrammarRuleStateTransitionType(IntFlag):
    SGRSTTEpsilon = 0
    SGRSTTWord = 1
    SGRSTTRule = 2
    SGRSTTDictation = 3
    SGRSTTWildcard = 4
    SGRSTTTextBuffer = 5


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


class DISPID_SpeechMMSysAudio(IntFlag):
    DISPID_SMSADeviceId = 300
    DISPID_SMSALineId = 301
    DISPID_SMSAMMHandle = 302


class SpeechVoicePriority(IntFlag):
    SVPNormal = 0
    SVPAlert = 1
    SVPOver = 2


class DISPID_SpeechMemoryStream(IntFlag):
    DISPID_SMSSetData = 100
    DISPID_SMSGetData = 101


class DISPID_SpeechFileStream(IntFlag):
    DISPID_SFSOpen = 100
    DISPID_SFSClose = 101


class DISPID_SpeechCustomStream(IntFlag):
    DISPID_SCSBaseStream = 100


class DISPID_SpeechPhraseProperties(IntFlag):
    DISPID_SPPsCount = 1
    DISPID_SPPsItem = 0
    DISPID_SPPs_NewEnum = -4


class DISPID_SpeechAudioStatus(IntFlag):
    DISPID_SASFreeBufferSpace = 1
    DISPID_SASNonBlockingIO = 2
    DISPID_SASState = 3
    DISPID_SASCurrentSeekPosition = 4
    DISPID_SASCurrentDevicePosition = 5


class DISPID_SpeechPhraseRule(IntFlag):
    DISPID_SPRuleName = 1
    DISPID_SPRuleId = 2
    DISPID_SPRuleFirstElement = 3
    DISPID_SPRuleNumberOfElements = 4
    DISPID_SPRuleParent = 5
    DISPID_SPRuleChildren = 6
    DISPID_SPRuleConfidence = 7
    DISPID_SPRuleEngineConfidence = 8


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


class DISPID_SpeechAudioBufferInfo(IntFlag):
    DISPID_SABIMinNotification = 1
    DISPID_SABIBufferSize = 2
    DISPID_SABIEventBias = 3


class DISPID_SpeechPhraseRules(IntFlag):
    DISPID_SPRulesCount = 1
    DISPID_SPRulesItem = 0
    DISPID_SPRules_NewEnum = -4


class SpeechWordType(IntFlag):
    SWTAdded = 1
    SWTDeleted = 2


class DISPID_SpeechWaveFormatEx(IntFlag):
    DISPID_SWFEFormatTag = 1
    DISPID_SWFEChannels = 2
    DISPID_SWFESamplesPerSec = 3
    DISPID_SWFEAvgBytesPerSec = 4
    DISPID_SWFEBlockAlign = 5
    DISPID_SWFEBitsPerSample = 6
    DISPID_SWFEExtraData = 7


class DISPID_SpeechLexicon(IntFlag):
    DISPID_SLGenerationId = 1
    DISPID_SLGetWords = 2
    DISPID_SLAddPronunciation = 3
    DISPID_SLAddPronunciationByPhoneIds = 4
    DISPID_SLRemovePronunciation = 5
    DISPID_SLRemovePronunciationByPhoneIds = 6
    DISPID_SLGetPronunciations = 7
    DISPID_SLGetGenerationChange = 8


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


class SpeechRecoContextState(IntFlag):
    SRCS_Disabled = 0
    SRCS_Enabled = 1


class SpeechRetainedAudioOptions(IntFlag):
    SRAONone = 0
    SRAORetainAudio = 1


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


class SPAUDIOOPTIONS(IntFlag):
    SPAO_NONE = 0
    SPAO_RETAIN_AUDIO = 1


class SPBOOKMARKOPTIONS(IntFlag):
    SPBO_NONE = 0
    SPBO_PAUSE = 1
    SPBO_AHEAD = 2
    SPBO_TIME_UNITS = 4


class SPCONTEXTSTATE(IntFlag):
    SPCS_DISABLED = 0
    SPCS_ENABLED = 1


class SpeechDisplayAttributes(IntFlag):
    SDA_No_Trailing_Space = 0
    SDA_One_Trailing_Space = 2
    SDA_Two_Trailing_Spaces = 4
    SDA_Consume_Leading_Spaces = 8


class DISPID_SpeechLexiconWords(IntFlag):
    DISPID_SLWsCount = 1
    DISPID_SLWsItem = 0
    DISPID_SLWs_NewEnum = -4


class SPRECOSTATE(IntFlag):
    SPRST_INACTIVE = 0
    SPRST_ACTIVE = 1
    SPRST_ACTIVE_ALWAYS = 2
    SPRST_INACTIVE_WITH_PURGE = 3
    SPRST_NUM_STATES = 4


class SPWAVEFORMATTYPE(IntFlag):
    SPWF_INPUT = 0
    SPWF_SRENGINE = 1


class DISPID_SpeechLexiconWord(IntFlag):
    DISPID_SLWLangId = 1
    DISPID_SLWType = 2
    DISPID_SLWWord = 3
    DISPID_SLWPronunciations = 4


class DISPID_SpeechLexiconProns(IntFlag):
    DISPID_SLPsCount = 1
    DISPID_SLPsItem = 0
    DISPID_SLPs_NewEnum = -4


class SpeechLoadOption(IntFlag):
    SLOStatic = 0
    SLODynamic = 1


class DISPID_SpeechLexiconPronunciation(IntFlag):
    DISPID_SLPType = 1
    DISPID_SLPLangId = 2
    DISPID_SLPPartOfSpeech = 3
    DISPID_SLPPhoneIds = 4
    DISPID_SLPSymbolic = 5


class SpeechRunState(IntFlag):
    SRSEDone = 1
    SRSEIsSpeaking = 2


class SPFILEMODE(IntFlag):
    SPFM_OPEN_READONLY = 0
    SPFM_OPEN_READWRITE = 1
    SPFM_CREATE = 2
    SPFM_CREATE_ALWAYS = 3
    SPFM_NUM_MODES = 4


class SpeechRuleState(IntFlag):
    SGDSInactive = 0
    SGDSActive = 1
    SGDSActiveWithAutoPause = 3
    SGDSActiveUserDelimited = 4


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


class DISPID_SpeechPhoneConverter(IntFlag):
    DISPID_SPCLangId = 1
    DISPID_SPCPhoneToId = 2
    DISPID_SPCIdToPhone = 3


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


class SpeechWordPronounceable(IntFlag):
    SWPUnknownWordUnpronounceable = 0
    SWPUnknownWordPronounceable = 1
    SWPKnownWordPronounceable = 2


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


class SpeechStreamSeekPositionType(IntFlag):
    SSSPTRelativeToStart = 0
    SSSPTRelativeToCurrentPosition = 1
    SSSPTRelativeToEnd = 2


class SpeechAudioState(IntFlag):
    SASClosed = 0
    SASStop = 1
    SASPause = 2
    SASRun = 3


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


class SpeechGrammarState(IntFlag):
    SGSEnabled = 1
    SGSDisabled = 0
    SGSExclusive = 3


class SpeechEmulationCompareFlags(IntFlag):
    SECFIgnoreCase = 1
    SECFIgnoreKanaType = 65536
    SECFIgnoreWidth = 131072
    SECFNoSpecialChars = 536870912
    SECFEmulateResult = 1073741824
    SECFDefault = 196609


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


class DISPID_SpeechRecognizerStatus(IntFlag):
    DISPID_SRSAudioStatus = 1
    DISPID_SRSCurrentStreamPosition = 2
    DISPID_SRSCurrentStreamNumber = 3
    DISPID_SRSNumberOfActiveRules = 4
    DISPID_SRSClsidEngine = 5
    DISPID_SRSSupportedLanguages = 6


class SpeechStreamFileMode(IntFlag):
    SSFMOpenForRead = 0
    SSFMOpenReadWrite = 1
    SSFMCreate = 2
    SSFMCreateForWrite = 3


class SPSEMANTICFORMAT(IntFlag):
    SPSMF_SAPI_PROPERTIES = 0
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS = 1
    SPSMF_SRGS_SAPIPROPERTIES = 2
    SPSMF_UPS = 4
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C = 8


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


class DISPID_SpeechPhraseAlternates(IntFlag):
    DISPID_SPAsCount = 1
    DISPID_SPAsItem = 0
    DISPID_SPAs_NewEnum = -4


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


class SPXMLRESULTOPTIONS(IntFlag):
    SPXRO_SML = 0
    SPXRO_Alternates_SML = 1


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


class DISPID_SpeechGrammarRule(IntFlag):
    DISPID_SGRAttributes = 1
    DISPID_SGRInitialState = 2
    DISPID_SGRName = 3
    DISPID_SGRId = 4
    DISPID_SGRClear = 5
    DISPID_SGRAddResource = 6
    DISPID_SGRAddState = 7


class SPADAPTATIONRELEVANCE(IntFlag):
    SPAR_Unknown = 0
    SPAR_Low = 1
    SPAR_Medium = 2
    SPAR_High = 3


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


class DISPID_SpeechGrammarRules(IntFlag):
    DISPID_SGRsCount = 1
    DISPID_SGRsDynamic = 2
    DISPID_SGRsAdd = 3
    DISPID_SGRsCommit = 4
    DISPID_SGRsCommitAndSave = 5
    DISPID_SGRsFindRule = 6
    DISPID_SGRsItem = 0
    DISPID_SGRs_NewEnum = -4


class DISPID_SpeechGrammarRuleState(IntFlag):
    DISPID_SGRSRule = 1
    DISPID_SGRSTransitions = 2
    DISPID_SGRSAddWordTransition = 3
    DISPID_SGRSAddRuleTransition = 4
    DISPID_SGRSAddSpecialTransition = 5


class DISPID_SpeechGrammarRuleStateTransitions(IntFlag):
    DISPID_SGRSTsCount = 1
    DISPID_SGRSTsItem = 0
    DISPID_SGRSTs_NewEnum = -4


class DISPID_SpeechGrammarRuleStateTransition(IntFlag):
    DISPID_SGRSTType = 1
    DISPID_SGRSTText = 2
    DISPID_SGRSTRule = 3
    DISPID_SGRSTWeight = 4
    DISPID_SGRSTPropertyName = 5
    DISPID_SGRSTPropertyId = 6
    DISPID_SGRSTPropertyValue = 7
    DISPID_SGRSTNextState = 8


class SpeechTokenShellFolder(IntFlag):
    STSF_AppData = 26
    STSF_LocalAppData = 28
    STSF_CommonAppData = 35
    STSF_FlagCreate = 32768


class SPWORDTYPE(IntFlag):
    eWORDTYPE_ADDED = 1
    eWORDTYPE_DELETED = 2


class DISPIDSPTSI(IntFlag):
    DISPIDSPTSI_ActiveOffset = 1
    DISPIDSPTSI_ActiveLength = 2
    DISPIDSPTSI_SelectionOffset = 3
    DISPIDSPTSI_SelectionLength = 4


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


class SpeechTokenContext(IntFlag):
    STCInprocServer = 1
    STCInprocHandler = 2
    STCLocalServer = 4
    STCRemoteServer = 16
    STCAll = 23


class SPSHORTCUTTYPE(IntFlag):
    SPSHT_NotOverriden = -1
    SPSHT_Unknown = 0
    SPSHT_EMAIL = 4096
    SPSHT_OTHER = 8192
    SPPS_RESERVED1 = 12288
    SPPS_RESERVED2 = 16384
    SPPS_RESERVED3 = 20480
    SPPS_RESERVED4 = 61440


class DISPID_SpeechXMLRecoResult(IntFlag):
    DISPID_SRRGetXMLResult = 10
    DISPID_SRRGetXMLErrorInfo = 11


class SpeechDataKeyLocation(IntFlag):
    SDKLDefaultLocation = 0
    SDKLCurrentUser = 1
    SDKLLocalMachine = 2
    SDKLCurrentConfig = 5


class DISPID_SpeechRecoResult2(IntFlag):
    DISPID_SRRSetTextFeedback = 12


class SPCATEGORYTYPE(IntFlag):
    SPCT_COMMAND = 0
    SPCT_DICTATION = 1
    SPCT_SLEEP = 2
    SPCT_SUB_COMMAND = 3
    SPCT_SUB_DICTATION = 4


class DISPID_SpeechPhraseBuilder(IntFlag):
    DISPID_SPPBRestorePhraseFromMemory = 1


class DISPID_SpeechRecoResultTimes(IntFlag):
    DISPID_SRRTStreamTime = 1
    DISPID_SRRTLength = 2
    DISPID_SRRTTickCount = 3
    DISPID_SRRTOffsetFromStart = 4


class DISPID_SpeechPhraseAlternate(IntFlag):
    DISPID_SPARecoResult = 1
    DISPID_SPAStartElementInResult = 2
    DISPID_SPANumberOfElementsInResult = 3
    DISPID_SPAPhraseInfo = 4
    DISPID_SPACommit = 5


SPAUDIOSTATE = _SPAUDIOSTATE
SPSTREAMFORMATTYPE = SPWAVEFORMATTYPE


__all__ = [
    'SpeechPropertyHighConfidenceThreshold', 'eLEXTYPE_PRIVATE10',
    'SAFT22kHz16BitMono', 'SPEI_RECO_STATE_CHANGE',
    'SpeechPropertyComplexResponseSpeed', 'SPGRAMMARSTATE',
    'DISPID_SRCCreateGrammar', 'DISPID_SpeechFileStream',
    'DISPID_SDKSetStringValue', 'SpeechRecoContextState',
    'SPEI_SENTENCE_BOUNDARY', 'DISPID_SPRuleParent',
    'DISPID_SRGSetWordSequenceData',
    'DISPID_SRCEPropertyNumberChange', 'SPEVENT',
    'SGLexicalNoSpecialChars', 'DISPID_SAVolume',
    'IInternetSecurityManager', 'SWPKnownWordPronounceable',
    'DISPID_SDKGetlongValue', 'DISPID_SVSInputSentencePosition',
    'DISPID_SGRSAddWordTransition', 'DISPID_SVAudioOutput',
    'SSSPTRelativeToEnd', 'DISPID_SPARecoResult', 'SPSNoun',
    'SPGRAMMARWORDTYPE', 'SpeechAudioVolume',
    'DISPID_SASFreeBufferSpace', 'DISPID_SLGenerationId',
    'SPSERIALIZEDRESULT', 'DISPID_SGRsDynamic', 'DISPID_SGRSTText',
    'ISpeechPhraseReplacements', 'SPRECOCONTEXTSTATUS',
    'DISPID_SPRuleNumberOfElements', 'SREPropertyStringChange',
    'SAFTGSM610_11kHzMono', 'DISPIDSPTSI_ActiveLength',
    'DISPID_SRRAudio', 'SPINTERFERENCE_NOSIGNAL',
    'DISPID_SVSLastResult', 'DISPID_SRGetRecognizers',
    'DISPID_SRGCmdSetRuleIdState', 'ISpeechPhraseInfoBuilder',
    'eWORDTYPE_DELETED', 'SPAR_High', 'SGDSActiveUserDelimited',
    'DISPID_SRAudioInputStream', 'DISPID_SRProfile',
    'SAFT12kHz8BitMono', 'DISPID_SGRsFindRule',
    'DISPID_SPERetainedSizeBytes', 'SPDKL_CurrentConfig', 'SPAS_RUN',
    'DISPID_SGRSRule', 'SpeechTokenKeyAttributes', 'SPRST_NUM_STATES',
    'SP_VISEME_4', 'SSFMCreate', 'DISPID_SRRPhraseInfo',
    'DISPID_SOTGetAttribute', 'SPWORDPRONOUNCEABLE', 'Library',
    'SPAO_RETAIN_AUDIO', 'SPWT_PRONUNCIATION', 'SDKLCurrentConfig',
    'SPEI_MAX_TTS', 'eLEXTYPE_PRIVATE6', 'SPEI_SR_AUDIO_LEVEL',
    'SVP_2', 'SPWF_SRENGINE', 'SDKLCurrentUser',
    'DISPID_SRRAlternates', 'SDTLexicalForm', 'SPCONTEXTSTATE',
    'SPWORD', 'SAFTCCITT_ALaw_11kHzMono', 'SGDSActive',
    'SPGS_ENABLED', 'SPFM_OPEN_READWRITE', 'DISPID_SpeechBaseStream',
    'SPRECOGNIZERSTATUS', 'SPRULESTATE', 'ISpLexicon',
    'SVSFPersistXML', 'DISPID_SFSOpen', 'SPRULE', 'DISPID_SLPType',
    'eLEXTYPE_PRIVATE3', 'DISPID_SBSWrite',
    'DISPID_SRCCmdMaxAlternates', 'DISPID_SWFEChannels',
    'DISPID_SPACommit', 'SPEVENTSOURCEINFO', 'ISpeechPhraseAlternate',
    'DISPID_SPRulesItem', 'ISpGrammarBuilder', 'SPGS_DISABLED',
    'SAFT11kHz8BitMono', 'SAFTText', 'ISpXMLRecoResult',
    'DISPID_SVStatus', 'ISpObjectTokenCategory', 'ISpPhrase',
    'DISPID_SLRemovePronunciationByPhoneIds',
    'DISPID_SRGIsPronounceable', 'SpeechVoiceSkipTypeSentence',
    'DISPID_SRCERequestUI', 'SAFT24kHz16BitStereo',
    'SAFTCCITT_uLaw_22kHzMono', 'SpeechWordPronounceable',
    'SP_VISEME_15', 'SAFT22kHz16BitStereo', 'DISPID_SRIsShared',
    'DISPID_SPEActualConfidence', 'SpeechWordType', 'SRSEIsSpeaking',
    'Speech_StreamPos_Asap', 'DISPID_SRGetFormat', 'SP_VISEME_13',
    'SGRSTTTextBuffer', 'DISPID_SAEventHandle',
    'DISPID_SRSetPropertyNumber', 'SVP_14', 'SRESoundEnd',
    'DISPID_SRRAudioFormat', 'SDTReplacement',
    'DISPID_SRGCmdLoadFromResource', 'DISPID_SPEPronunciation',
    'ISpeechGrammarRuleStateTransition', 'ISpeechPhraseElement',
    'SpeechPropertyLowConfidenceThreshold', 'SVP_17', 'SVP_12',
    'SDTRule', 'SPEI_TTS_BOOKMARK', 'SRATopLevel',
    'DISPID_SDKSetLongValue', 'DISPID_SRGCommit',
    'SpeechVoiceSpeakFlags', 'SAFT8kHz16BitStereo',
    'SAFT12kHz8BitStereo', 'ISpeechLexicon', 'DISPID_SGRsCommit',
    'SECHighConfidence', 'SVEWordBoundary',
    'ISpeechPhraseReplacement',
    '__MIDL___MIDL_itf_sapi_0000_0020_0002',
    'DISPID_SGRSAddSpecialTransition', 'DISPID_SRRSetTextFeedback',
    'SpeechFormatType', 'SPBO_NONE', 'SVF_None', 'SpeechInterference',
    'SGRSTTRule', 'SVPAlert', 'SREStreamEnd', 'SPEI_TTS_AUDIO_LEVEL',
    'SPRECORESULTTIMES', 'SVSFParseAutodetect', 'SPXMLRESULTOPTIONS',
    'eLEXTYPE_PRIVATE13', 'ISpEventSource', 'DISPID_SPIRule',
    'SAFTNoAssignedFormat', 'SpeechVoiceEvents', 'SpeechPartOfSpeech',
    'SPVPRI_NORMAL', 'DISPID_SASetState', 'DISPID_SVGetAudioInputs',
    'SAFT11kHz16BitMono', 'DISPID_SRCEventInterests',
    'SpeechRecoEvents', 'STSF_CommonAppData', 'ISpeechPhraseRule',
    'SP_VISEME_6', 'SDKLDefaultLocation', 'DISPID_SpeechAudio',
    'ISpRecoContext', 'DISPID_SOTCGetDataKey', 'SRTSMLTimeout',
    'SGSExclusive', 'DISPID_SRRSaveToMemory',
    'DISPID_SWFESamplesPerSec',
    'DISPID_SVAllowAudioOuputFormatChangesOnNextSet', 'SRESoundStart',
    'DISPID_SPEDisplayText', 'DISPID_SGRName', 'SVP_21',
    'DISPID_SPIEnginePrivateData', 'SP_VISEME_19',
    'SAFTCCITT_uLaw_22kHzStereo', 'SPRST_ACTIVE_ALWAYS',
    'SPAR_Unknown', 'SPXRO_Alternates_SML', 'eLEXTYPE_PRIVATE16',
    'DISPID_SPAsItem', 'SpeechAudioProperties', 'DISPID_SLWsItem',
    'SRSInactive', 'DISPID_SPISaveToMemory', 'Speech_Max_Word_Length',
    'SAFTCCITT_ALaw_44kHzMono', 'SpStreamFormatConverter',
    'SPWORDTYPE', 'SPCT_DICTATION', 'SVSFVoiceMask', 'SPWF_INPUT',
    'DISPID_SpeechPhoneConverter', 'SPEI_PROPERTY_NUM_CHANGE',
    'DISPID_SGRSTransitions', 'SpeechStreamFileMode',
    'DISPID_SGRSAddRuleTransition', 'SVEAudioLevel', 'SVP_5',
    'SAFTCCITT_ALaw_22kHzMono', 'SpPhoneticAlphabetConverter',
    'DISPID_SVSLastBookmarkId', 'DISPID_SpeechDataKey',
    'SPAUDIOOPTIONS', 'SpeechPropertyNormalConfidenceThreshold',
    'SpeechEmulationCompareFlags', 'DISPID_SOTRemoveStorageFileName',
    'SPEI_SR_PRIVATE', 'DISPID_SOTGetDescription',
    'Speech_Default_Weight', 'DISPID_SDKEnumValues',
    'ISpObjectWithToken', 'DISPID_SpeechCustomStream',
    'DISPID_SVSyncronousSpeakTimeout', 'DISPID_SRStatus',
    'DISPID_SPPParent', 'ISpeechRecoResultTimes', 'SVP_8',
    'SPRST_INACTIVE_WITH_PURGE', 'SVSFNLPMask',
    'SPDKL_DefaultLocation', 'SpInProcRecoContext', 'SRAImport',
    'SP_VISEME_21', 'SVP_16', 'DISPID_SVSpeakStream', 'SP_VISEME_5',
    'SpeechUserTraining', 'DISPID_SRCRequestedUIType',
    'DISPID_SpeechAudioBufferInfo', 'SECFIgnoreKanaType',
    'SRSInactiveWithPurge', 'SVSFIsNotXML', 'DISPID_SPRuleConfidence',
    'SpeechPropertyResourceUsage', 'DISPIDSPTSI_ActiveOffset',
    'DISPID_SVSpeak', 'DISPID_SRGCmdLoadFromFile', 'SRAExport',
    'SECFDefault', 'SPWAVEFORMATTYPE', 'SDA_One_Trailing_Space',
    'ISpeechGrammarRuleState', 'SPFM_NUM_MODES',
    'SPSMF_SAPI_PROPERTIES', 'SDTAlternates', 'SpeechVisemeType',
    'SpeechTokenShellFolder', 'DISPID_SRState', 'DISPID_SRCState',
    'eLEXTYPE_RESERVED6', 'DISPID_SGRSTRule',
    'SpeechCategoryAppLexicons', 'SPAS_CLOSED', 'SpCompressedLexicon',
    'SpeechAudioFormatType', 'SpeechTokenContext',
    'DISPID_SOTIsUISupported', 'SGRSTTWord', 'SpeechCategoryVoices',
    'DISPID_SpeechPhraseRules', 'SAFT8kHz8BitMono',
    'SpeechCategoryRecognizers', 'IEnumSpObjectTokens', 'SVP_3',
    'SINoise', 'DISPID_SpeechLexiconWord',
    'SPRS_ACTIVE_USER_DELIMITED', 'SpUnCompressedLexicon',
    'DISPID_SOTCategory', 'SPAO_NONE', 'DISPID_SPIGetText',
    'ISpNotifyTranslator', 'DISPID_SADefaultFormat', 'eLEXTYPE_APP',
    'DISPID_SRRGetXMLResult', '_ISpeechRecoContextEvents', 'SVP_7',
    'DISPID_SLAddPronunciationByPhoneIds', 'DISPID_SGRSTs_NewEnum',
    'SPINTERFERENCE_NONE', 'DISPID_SVPriority', 'SPPHRASEPROPERTY',
    'SPEI_MIN_SR', 'DISPID_SpeechLexiconPronunciation',
    'SpeechTokenKeyFiles', 'DISPID_SPRuleFirstElement',
    'DISPID_SpeechPhraseElement', 'SPEI_VISEME',
    'SREFalseRecognition', 'DISPID_SPAPhraseInfo', 'DISPID_SPCLangId',
    'DISPID_SASNonBlockingIO', 'DISPID_SVResume', 'SPLO_DYNAMIC',
    'DISPID_SGRSTNextState', 'SSTTWildcard', 'ISpeechPhraseRules',
    'SPPROPERTYINFO', 'DISPID_SPELexicalForm',
    'SAFTCCITT_uLaw_44kHzStereo', 'SREInterference',
    'ISpPhoneticAlphabetConverter', 'DISPID_SPEEngineConfidence',
    'SpeechGrammarTagWildcard', 'eLEXTYPE_LETTERTOSOUND',
    'SpeechDiscardType', 'SPWP_UNKNOWN_WORD_PRONOUNCEABLE',
    'SRTStandard', 'SpeechDisplayAttributes', 'ISpeechPhraseElements',
    'DISPID_SGRs_NewEnum', 'SAFTTrueSpeech_8kHz1BitMono',
    'SAFT8kHz16BitMono', 'SP_VISEME_8', 'SAFTCCITT_uLaw_44kHzMono',
    'SRADefaultToActive', 'SPEI_FALSE_RECOGNITION',
    'DISPID_SLPSymbolic', 'SPFM_CREATE_ALWAYS',
    'SAFTCCITT_ALaw_11kHzStereo', 'SREPrivate',
    'DISPID_SDKSetBinaryValue', 'SVP_4', 'DISPID_SVSLastBookmark',
    'DISPID_SPCPhoneToId', 'ISpRecognizer3', 'SVF_Stressed',
    'SAFTGSM610_8kHzMono', 'DISPID_SRSSupportedLanguages',
    'DISPID_SPILanguageId', 'SREBookmark', 'DISPID_SLPsItem',
    'DISPID_SLWs_NewEnum', 'eLEXTYPE_PRIVATE20',
    'DISPID_SPRDisplayAttributes', 'eLEXTYPE_PRIVATE7', 'SPBO_AHEAD',
    'eLEXTYPE_PRIVATE11', 'SPINTERFERENCE_LATENCY_WARNING',
    'SpeechDictationTopicSpelling', 'SpeechTokenKeyUI',
    'ISpPhoneConverter', 'SPLO_STATIC',
    'DISPID_SPERetainedStreamOffset', 'SPEI_RESERVED5',
    'DISPID_SLWType', 'DISPID_SPPChildren', 'SPBINARYGRAMMAR',
    'SAFT8kHz8BitStereo', 'SPCATEGORYTYPE', 'SREStateChange',
    'ISpeechPhraseProperties', 'SPWT_LEXICAL',
    'SPSMF_SRGS_SAPIPROPERTIES', 'SAFTDefault',
    'IInternetSecurityMgrSite', 'DISPID_SDKGetBinaryValue',
    'SAFTGSM610_44kHzMono', 'DISPID_SpeechAudioStatus',
    'DISPID_SABufferNotifySize', 'DISPID_SVEStreamStart',
    'DISPID_SRGCmdLoadFromMemory', 'SRAONone', 'DISPID_SRCEBookmark',
    'SPSVerb', 'DISPID_SGRsCount', 'DISPID_SVSCurrentStreamNumber',
    'DISPID_SVEAudioLevel', 'SP_VISEME_1', 'DISPID_SDKCreateKey',
    'SAFT11kHz8BitStereo', 'SWTAdded', 'ISpeechLexiconPronunciation',
    'ISpeechRecoContext', 'DISPID_SRCBookmark', 'DISPID_SOTRemove',
    'SPBOOKMARKOPTIONS', 'SVSFNLPSpeakPunc', 'SPRST_ACTIVE',
    'ISpeechVoiceStatus', 'DISPID_SOTsItem', 'SECFIgnoreWidth',
    'DISPID_SPRNumberOfElements', 'DISPID_SABIMinNotification',
    'DISPID_SpeechVoice', 'DISPID_SVEBookmark', 'SREAllEvents',
    'SAFTCCITT_uLaw_11kHzMono', 'SPSMF_UPS', 'SPSLMA',
    'SSFMOpenReadWrite', 'DISPID_SRCEAdaptation',
    'DISPID_SOTs_NewEnum', 'DISPID_SVWaitUntilDone', 'SVP_15',
    'DISPID_SRSCurrentStreamNumber', 'DISPID_SPPsCount',
    'DISPID_SRCEHypothesis',
    'DISPID_SpeechGrammarRuleStateTransitions', 'SREAudioLevel',
    'DISPID_SVEventInterests', 'DISPID_SRCEPropertyStringChange',
    'SpeechEngineConfidence', 'DISPID_SRGetPropertyString',
    'SAFTCCITT_ALaw_8kHzMono', 'DISPID_SPRuleChildren',
    'DISPID_SCSBaseStream', 'SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE',
    'SPEI_UNDEFINED', 'SVSFIsXML', 'DISPID_SOTCId',
    'DISPID_SWFEFormatTag', 'DISPID_SVSInputWordPosition',
    'ISpeechTextSelectionInformation', 'SAFT16kHz8BitMono',
    'SVEPrivate', 'SAFT44kHz16BitStereo',
    'SWPUnknownWordPronounceable', 'DISPID_SPIEngineId',
    'SPSFunction', 'SpeechPropertyResponseSpeed',
    'DISPID_SRCCreateResultFromMemory', 'DISPID_SRDisplayUI',
    'SITooSlow', 'DISPID_SREmulateRecognition',
    'SPINTERFERENCE_TOOFAST', 'DISPID_SRGetPropertyNumber',
    'SPEI_RESERVED1', 'SECFIgnoreCase',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_MS', 'SAFT44kHz16BitMono',
    'Speech_StreamPos_RealTime', 'STCInprocHandler', 'SRERequestUI',
    'SVPOver', 'STSF_LocalAppData', 'SPEI_ADAPTATION',
    'ISpResourceManager', 'ISpEventSink', 'SP_VISEME_10',
    'SWTDeleted', 'SPSUnknown', 'SPVPRIORITY', 'SpeechGrammarState',
    'SpeechRecognizerState', 'SAFT12kHz16BitStereo',
    'ISpNotifySource', 'DISPID_SOTMatchesAttributes',
    'SAFTADPCM_8kHzMono', '_SPAUDIOSTATE',
    'DISPID_SRGSetTextSelection', 'eLEXTYPE_RESERVED10',
    'SAFTNonStandardFormat', 'DISPID_SRRDiscardResultInfo',
    'SVEVoiceChange', 'SPRS_ACTIVE_WITH_AUTO_PAUSE', 'SPPS_Verb',
    'DISPID_SRGState', 'SAFT24kHz8BitStereo', 'SPPS_Modifier',
    'DISPID_SLWsCount', 'DISPID_SPEAudioStreamOffset',
    'DISPID_SDKDeleteValue', 'SAFT24kHz16BitMono', 'SITooLoud',
    'SVEEndInputStream', 'DISPID_SDKEnumKeys', 'eLEXTYPE_PRIVATE2',
    'ISpeechResourceLoader', 'DISPID_SVSRunningState',
    'DISPID_SRCAudioInInterferenceStatus', 'DISPID_SGRClear',
    'DISPID_SPPBRestorePhraseFromMemory', 'DISPID_SVEPhoneme',
    'SpeechRecognitionType', 'SPPHRASE', 'ISpSerializeState',
    'DISPID_SpeechPhraseRule', 'ISpRecognizer2',
    'DISPID_SWFEExtraData', 'DISPID_SPEAudioSizeTime',
    'SpCustomStream', 'SpeechPropertyAdaptationOn', 'SASPause',
    'SpeechDataKeyLocation', 'SVP_9', 'SRERecognition',
    'ISpStreamFormat', 'SPEI_SOUND_END', 'ISpeechAudio',
    'tagSPPROPERTYINFO', 'DISPID_SRSCurrentStreamPosition',
    'DISPID_SMSAMMHandle', 'DISPID_SPAsCount',
    'DISPID_SLGetGenerationChange', 'SPSHT_NotOverriden',
    'SSSPTRelativeToCurrentPosition', 'DISPID_SRGRecoContext',
    'DISPID_SDKDeleteKey', 'DISPID_SPRuleName',
    'DISPID_SPIReplacements', 'DISPID_SASCurrentSeekPosition',
    'DISPID_SFSClose', 'SPFM_OPEN_READONLY', 'SPCT_SLEEP',
    'DISPID_SAStatus', 'SPEI_MIN_TTS',
    'DISPID_SpeechPhraseProperties', 'DISPID_SPRFirstElement',
    'DISPID_SVEWord', 'SVP_10', 'SpWaveFormatEx',
    'DISPID_SpeechObjectTokenCategory', 'DISPID_SpeechRecoResult2',
    'DISPID_SVESentenceBoundary', 'SAFTCCITT_ALaw_8kHzStereo',
    'SPEI_VOICE_CHANGE', 'SAFT12kHz16BitMono', 'SPPS_RESERVED4',
    'SPRST_INACTIVE', 'eLEXTYPE_PRIVATE14', 'SDKLLocalMachine',
    'SPINTERFERENCE', 'DISPID_SPIAudioStreamPosition',
    'DISPID_SRCVoicePurgeEvent', 'ISpRecoGrammar', 'SASStop',
    'SPAR_Low', 'SPEI_TTS_PRIVATE', 'DISPID_SPRText',
    'DISPID_SAFGetWaveFormatEx', 'DISPID_SPRuleId',
    'DISPID_SPRs_NewEnum', 'DISPID_SpeechMemoryStream',
    'SpMMAudioEnum', 'SPXRO_SML', 'SAFT32kHz16BitStereo',
    'SPPS_RESERVED1', 'ISpeechLexiconWords', 'SDA_No_Trailing_Space',
    'SPCT_SUB_COMMAND', 'DISPID_SPRules_NewEnum', 'ISpRecoContext2',
    'SVP_19', 'SpeechTokenIdUserLexicon', 'DISPID_SpeechMMSysAudio',
    'DISPID_SRRTimes', 'DISPID_SpeechGrammarRules', 'SSTTDictation',
    'DISPID_SVVoice', 'SLOStatic', 'SAFTCCITT_uLaw_11kHzStereo',
    'SECLowConfidence', 'SPPS_Unknown', 'SpeechCategoryAudioOut',
    'SPINTERFERENCE_TOOLOUD', 'SPEI_ACTIVE_CATEGORY_CHANGED',
    'SP_VISEME_18', 'DISPID_SPIStartTime', 'SVEPhoneme',
    'SpeechStreamSeekPositionType', 'SREPhraseStart', 'ISpRecoResult',
    'SVSFPurgeBeforeSpeak', 'ISpeechGrammarRule', 'SGPronounciation',
    'SGLexical', 'SVSFlagsAsync', 'SAFTADPCM_44kHzMono',
    'ISpeechWaveFormatEx', 'SAFT32kHz8BitMono', 'SPPARTOFSPEECH',
    'SPEI_RESERVED3', 'SAFT32kHz8BitStereo',
    'ISpeechRecoResultDispatch', 'DISPID_SpeechVoiceStatus',
    'DISPID_SPEsItem', 'typelib_path', 'SVEBookmark', 'SFTInput',
    'DISPID_SRGCmdLoadFromProprietaryGrammar', 'STSF_AppData',
    'ISpeechObjectTokens', 'SP_VISEME_20', 'ISpRecoCategory',
    'DISPID_SRRTTickCount', 'SPEI_RESERVED2', 'SVP_1',
    'DISPID_SRRTOffsetFromStart', 'SpeechRuleAttributes', 'IStream',
    'SVP_0', 'DISPID_SOTId', 'SpFileStream', 'SSFMOpenForRead',
    'tagSTATSTG', 'SP_VISEME_12', 'DISPID_SPRulesCount',
    'SPTEXTSELECTIONINFO', 'DISPID_SVSVisemeId', 'LONG_PTR',
    'SRAInterpreter', 'SpVoice', 'SVP_11', 'eLEXTYPE_PRIVATE5',
    'SpeechTokenValueCLSID', 'DISPID_SLAddPronunciation',
    'DISPID_SpeechRecoResultTimes', 'SpMemoryStream',
    'SAFT22kHz8BitMono', 'SPDATAKEYLOCATION', 'ISpObjectToken',
    'DISPID_SVSpeakCompleteEvent', 'SPPS_Function',
    'SPWT_LEXICAL_NO_SPECIAL_CHARS', 'SASClosed', 'SRTReSent',
    'SGRSTTEpsilon', 'DISPID_SLWLangId', 'SPEI_START_SR_STREAM',
    'DISPID_SRRRecoContext', 'ISpeechAudioFormat', 'DISPID_SVRate',
    'DISPID_SRCRecognizer', 'SPEI_END_SR_STREAM', 'DISPID_SBSFormat',
    'SGSDisabled', 'SAFTADPCM_44kHzStereo', 'DISPID_SpeechRecoResult',
    '_RemotableHandle', 'DISPIDSPTSI_SelectionLength',
    'SPEI_HYPOTHESIS', 'DISPID_SGRsItem', 'ISpeechRecoGrammar',
    'SPLEXICONTYPE', 'DISPID_SRGCmdLoadFromObject',
    'DISPID_SRCERecognitionForOtherContext', 'SpeechAllElements',
    'SPBO_TIME_UNITS', 'SAFT44kHz8BitMono', 'SpeechAddRemoveWord',
    'DISPID_SpeechLexicon', 'SPRS_INACTIVE', 'SpeechLexiconType',
    'SVEStartInputStream', 'SpSharedRecognizer',
    'DISPID_SOTDisplayUI', 'SPBO_PAUSE', 'DISPID_SABIEventBias',
    'ISpeechGrammarRules', 'SINone', 'SpeechBookmarkOptions',
    'ISpPhoneticAlphabetSelection', 'SPAUDIOBUFFERINFO',
    'eLEXTYPE_PRIVATE17', 'DISPID_SGRAddResource',
    'DISPID_SRCEStartStream', 'DISPID_SRGDictationLoad',
    'DISPID_SpeechGrammarRuleStateTransition', 'SITooFast',
    'SPEI_RECOGNITION', 'SGRSTTWildcard',
    'DISPID_SOTCEnumerateTokens', 'SPCT_COMMAND',
    'DISPID_SRCERecognition', 'SPGS_EXCLUSIVE', 'DISPID_SPPsItem',
    'SDTProperty', 'DISPID_SLGetPronunciations',
    'DISPID_SRCRetainedAudio', 'SRSActive',
    'DISPID_SVSLastStreamNumberQueued',
    'DISPID_SpeechPhraseReplacements', 'eLEXTYPE_PRIVATE18',
    'DISPID_SVEViseme', 'WAVEFORMATEX', 'SpeechAudioState',
    'DISPID_SRCEEndStream', 'DISPID_SPIElements', 'SVSFUnusedFlags',
    'DISPID_SRCESoundStart', 'SpeechSpecialTransitionType',
    'SDTAudio', 'ISpeechRecoResult', 'SpeechRegistryUserRoot',
    'SAFTCCITT_uLaw_8kHzMono', 'SECFNoSpecialChars',
    'SPEI_RECO_OTHER_CONTEXT', 'DISPID_SpeechVoiceEvent',
    'DISPID_SWFEBlockAlign', 'SPDKL_CurrentUser',
    'SWPUnknownWordUnpronounceable', 'DISPID_SGRId',
    'DISPID_SDKGetStringValue', 'DISPID_SLPPartOfSpeech',
    'SAFT24kHz8BitMono', 'SpObjectTokenCategory',
    'SAFTCCITT_ALaw_22kHzStereo', 'SAFTADPCM_11kHzStereo',
    'SGSEnabled', 'SPEI_REQUEST_UI', 'SDTPronunciation',
    'ISpProperties', 'SRCS_Disabled', 'ISpVoice',
    'eLEXTYPE_RESERVED9', 'SPEVENTENUM', 'eLEXTYPE_PRIVATE9',
    'DISPID_SRCESoundEnd', 'eLEXTYPE_PRIVATE15',
    'DISPID_SpeechRecognizerStatus', 'DISPID_SBSSeek',
    'eLEXTYPE_PRIVATE12', 'DISPID_SGRsAdd',
    'SpeechVoiceCategoryTTSRate', 'DISPID_SVGetVoices',
    'SPPS_RESERVED2', 'DISPID_SVSPhonemeId',
    'DISPID_SRCSetAdaptationData', 'SAFT16kHz8BitStereo',
    'DISPID_SPEDisplayAttributes', 'DISPID_SpeechPhraseElements',
    'SPWORDLIST', 'DISPID_SRGCmdSetRuleState',
    'DISPID_SVGetAudioOutputs', 'DISPID_SpeechGrammarRuleState',
    'ISpeechRecoResult2', 'IEnumString', 'eLEXTYPE_USER_SHORTCUT',
    'DISPID_SGRAddState', 'SpeechAudioFormatGUIDText',
    'DISPID_SPIProperties', 'DISPID_SpeechObjectToken',
    'DISPID_SpeechPhraseProperty', 'SpInprocRecognizer',
    'SDA_Two_Trailing_Spaces', 'DISPID_SRRTLength', 'SRCS_Enabled',
    'ISpDataKey', 'SPPHRASERULE', 'DISPID_SOTGetStorageFileName',
    'SPINTERFERENCE_TOOSLOW', 'DISPID_SMSALineId',
    'ISpeechPhraseInfo', 'SPPHRASEELEMENT', 'DISPID_SABIBufferSize',
    'SPPS_NotOverriden', 'DISPID_SPPName', 'DISPID_SLWPronunciations',
    'SPVPRI_ALERT', 'SSTTTextBuffer', 'SBOPause',
    'SpeechCategoryPhoneConverters', 'ISpStreamFormatConverter',
    'DISPID_SRAllowVoiceFormatMatchingOnNextSet',
    'ISpeechAudioStatus', 'DISPID_SpeechRecoContextEvents',
    'SAFT22kHz8BitStereo', 'SPSModifier', 'DISPIDSPTSI',
    'DISPID_SVSInputSentenceLength', 'SpTextSelectionInformation',
    'SLTUser', 'DISPID_SRCEFalseRecognition',
    'DISPID_SVIsUISupported', 'DISPID_SpeechPhraseReplacement',
    'SpeechVisemeFeature', 'DISPID_SVSkip', 'SPLOADOPTIONS',
    'DISPID_SpeechPhraseAlternate', 'DISPID_SVSInputWordLength',
    'DISPID_SLPPhoneIds', 'ISpShortcut', 'DISPID_SRRecognizer',
    'SPWP_KNOWN_WORD_PRONOUNCEABLE', 'SAFT44kHz8BitStereo',
    'DISPID_SWFEAvgBytesPerSec', 'DISPID_SpeechLexiconWords',
    'SAFTCCITT_uLaw_8kHzStereo', 'DISPID_SRSClsidEngine',
    'DISPID_SPEsCount', 'DISPID_SMSADeviceId', 'DISPID_SPPId',
    'SPSHT_OTHER', 'UINT_PTR', 'STSF_FlagCreate',
    'DISPID_SpeechLexiconProns', 'SPSERIALIZEDPHRASE',
    'SPEI_RESERVED6', 'SVESentenceBoundary',
    'DISPID_SWFEBitsPerSample', 'SpLexicon', 'SPVPRI_OVER',
    'SpSharedRecoContext', 'SPEI_PHONEME', 'DISPID_SOTsCount',
    'SpMMAudioIn', 'DISPID_SAFSetWaveFormatEx', 'SPEI_INTERFERENCE',
    'SPEI_PHRASE_START', 'DISPID_SRCEEnginePrivate', 'SpObjectToken',
    'ISpeechLexiconPronunciations', 'DISPID_SRAudioInput',
    'SAFTGSM610_22kHzMono', 'ISpeechBaseStream', 'DISPID_SAFType',
    'DISPID_SpeechPhraseInfo', 'DISPID_SGRSTWeight', 'DISPID_SVPause',
    'eLEXTYPE_PRIVATE1', 'SITooQuiet', 'DISPID_SVEVoiceChange',
    'eLEXTYPE_PRIVATE8', 'DISPID_SRSNumberOfActiveRules',
    '__MIDL_IWinTypes_0009', 'SpeechGrammarTagUnlimitedDictation',
    'SLODynamic', 'SECNormalConfidence', 'SINoSignal',
    'ISpeechMMSysAudio', 'STCInprocServer',
    'DISPID_SPIAudioSizeBytes', 'SP_VISEME_14', 'SPWORDPRONUNCIATION',
    'SPEI_END_INPUT_STREAM', 'SpeechVoicePriority',
    'ISpeechPhraseAlternates', 'DISPID_SRGId', 'DISPID_SBSRead',
    'DISPIDSPTSI_SelectionOffset', 'STCAll', 'SpResourceManager',
    'DISPID_SLPsCount', 'DISPID_SPRuleEngineConfidence',
    'tagSPTEXTSELECTIONINFO', 'SPSHT_EMAIL', 'eLEXTYPE_PRIVATE4',
    'SAFT32kHz16BitMono', 'DISPID_SPPFirstElement', 'DISPID_SRCPause',
    'SP_VISEME_9', 'SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN',
    'SpeechCategoryAudioIn',
    'DISPID_SRAllowAudioInputFormatChangesOnNextSet',
    'DISPID_SGRsCommitAndSave', 'DISPID_SLPs_NewEnum',
    'eLEXTYPE_VENDORLEXICON', 'STCRemoteServer', 'SGDisplay',
    'SAFT11kHz16BitStereo', 'SPEI_PROPERTY_STRING_CHANGE',
    'SRTExtendableParse', 'SPAR_Medium', 'SAFT48kHz8BitStereo',
    'SPSHT_Unknown', 'ISpeechFileStream', 'SPFILEMODE',
    'DISPID_SOTCreateInstance', 'SP_VISEME_11', 'SVF_Emphasis',
    'DISPID_SPEs_NewEnum', 'SPSEMANTICERRORINFO', 'SPPS_SuppressWord',
    'SPRS_ACTIVE', 'SPAS_STOP', 'DISPID_SRRSpeakAudio',
    'ISpeechXMLRecoResult', 'DISPID_SRGReset', 'DISPID_SPAs_NewEnum',
    'SVEAllEvents', 'ISpMMSysAudio', 'DISPID_SGRAttributes',
    'SPRECOSTATE', 'SPADAPTATIONRELEVANCE', 'SVPNormal',
    'eWORDTYPE_ADDED', 'SPEI_SR_BOOKMARK', 'SRSActiveAlways',
    'DISPID_SVEEnginePrivate', 'DISPID_SPERequiredConfidence',
    'DISPID_SRCERecognizerStateChange', 'DISPID_SGRInitialState',
    'ISpeechAudioBufferInfo', '__MIDL___MIDL_itf_sapi_0000_0020_0001',
    'DISPID_SPRsItem', 'DISPID_SPPValue', 'SpeechGrammarTagDictation',
    'SVP_6', 'SpeechRunState', 'SAFT16kHz16BitMono',
    'ISpeechRecognizer', 'DISPID_SRSetPropertyString',
    'DISPID_SPPs_NewEnum', 'SpeechGrammarWordType', 'SVSFParseSsml',
    'eLEXTYPE_USER', 'SpNotifyTranslator', 'ISpeechDataKey',
    'SRSEDone', 'DISPID_SRCRetainedAudioFormat',
    'DISPID_SRRTStreamTime', 'DISPID_SRGDictationUnload',
    'ISpeechObjectTokenCategory', 'SRTAutopause',
    'SpeechCategoryRecoProfiles', 'SpeechRecoProfileProperties',
    'DISPID_SRCreateRecoContext', 'SAFTADPCM_22kHzStereo', 'ISpAudio',
    'SAFTADPCM_11kHzMono', 'DISPID_SRCEInterference',
    'DISPID_SPCIdToPhone', 'Speech_Max_Pron_Length',
    'DISPID_SRGRules', 'SDTAll', 'SREStreamStart',
    'DISPID_SMSGetData', 'SpeechEngineProperties', 'SPPS_Noncontent',
    'SDA_Consume_Leading_Spaces', 'SFTSREngine',
    'DISPID_SpeechPhraseAlternates', 'SSFMCreateForWrite',
    'eLEXTYPE_PRIVATE19', 'DISPID_SRCEAudioLevel',
    'SpeechAudioFormatGUIDWave', 'SPAS_PAUSE', 'SREAdaptation',
    'eLEXTYPE_RESERVED8', 'DISPID_SGRSTsItem',
    'DISPID_SGRSTPropertyName', 'SVSFDefault', 'SPEI_SOUND_START',
    'DISPID_SPIGetDisplayAttributes', 'SREPropertyNumChange',
    'DISPID_SPRsCount', 'SGDSInactive', 'SpStream', 'SpeechRuleState',
    'DISPID_SLPLangId', 'SRARoot', 'SPSEMANTICFORMAT',
    'DISPID_SASCurrentDevicePosition', 'SAFTExtendedAudioFormat',
    'SBONone', 'SVSFParseSapi', 'SREHypothesis', 'SP_VISEME_17',
    'SAFT48kHz16BitMono', 'SpeechGrammarRuleStateTransitionType',
    'SRTEmulated', 'SPSNotOverriden', 'DISPID_SABufferInfo',
    'SPEI_MAX_SR', 'SRERecoOtherContext', 'SpPhraseInfoBuilder',
    'SpeechRetainedAudioOptions', 'SPPS_Noun', 'SPSHORTCUTPAIR',
    'DISPIDSPRG', 'SPSInterjection', 'DISPID_SGRSTsCount',
    'ISpeechPhoneConverter', 'ISpeechLexiconWord',
    'DISPID_SRIsUISupported', 'SP_VISEME_3',
    'DISPID_SPEAudioSizeBytes', 'SpPhoneConverter',
    'ISpeechObjectToken', 'DISPID_SPIGrammarId',
    'SAFT16kHz16BitStereo', 'SVSFIsFilename',
    'DISPID_SVAlertBoundary', 'DISPID_SGRSTPropertyValue',
    'SSSPTRelativeToStart', 'ISpRecoGrammar2', '_ISpeechVoiceEvents',
    'DISPID_SRCEPhraseStart', 'SPSMF_SRGS_SEMANTICINTERPRETATION_W3C',
    'ISpStream', 'SPAUDIOSTATUS', 'SVSFParseMask',
    'SpeechMicTraining', 'SPINTERFERENCE_NOISE', 'SPWT_DISPLAY',
    'SPSSuppressWord', 'SPPS_Interjection', 'SVP_13', 'SLTApp',
    'DISPID_SRCResume', 'DISPID_SRRGetXMLErrorInfo', 'SPSHORTCUTTYPE',
    'DISPID_SPIRetainedSizeBytes', 'DISPID_SPEAudioTimeOffset',
    'DISPID_SPAStartElementInResult', 'ISpeechMemoryStream',
    'ISpeechPhraseProperty', 'SAFTADPCM_22kHzMono', 'SPAUDIOSTATE',
    'DISPID_SpeechWaveFormatEx', 'ISpRecognizer', 'SpAudioFormat',
    'DISPID_SRGDictationSetState', 'STCLocalServer', 'SASRun',
    'SECFEmulateResult', 'DISPID_SGRSTPropertyId',
    'SPEI_WORD_BOUNDARY', 'DISPID_SPPConfidence',
    'DISPID_SpeechRecoContext', 'SPFM_CREATE',
    'SPINTERFERENCE_TOOQUIET', 'SPVISEMES', 'SGDSActiveWithAutoPause',
    'DISPID_SLGetWords', 'DISPID_SOTCDefault', 'SPCT_SUB_DICTATION',
    'eLEXTYPE_RESERVED7', 'SP_VISEME_2', 'SPCS_DISABLED',
    'SP_VISEME_0', 'SpeechLoadOption', 'DISPID_SASState',
    'DISPID_SLWWord', 'SRADynamic', 'DISPID_SPIAudioSizeTime',
    'DISPID_SLRemovePronunciation', 'DISPID_SpeechGrammarRule',
    'DISPID_SDKOpenKey', 'SAFT48kHz16BitStereo',
    'eLEXTYPE_MORPHOLOGY', 'DISPID_SpeechXMLRecoResult',
    'DISPID_SVDisplayUI', 'DISPID_SPPEngineConfidence',
    'SPWORDPRONUNCIATIONLIST', 'DISPID_SGRSTType', 'ISpeechVoice',
    'SP_VISEME_16', 'SAFT48kHz8BitMono', 'SPDKL_LocalMachine',
    'SPEI_START_INPUT_STREAM', 'DISPID_SOTSetId',
    'SPSHORTCUTPAIRLIST', 'SVP_18', 'DISPID_SPPNumberOfElements',
    'ISpeechCustomStream', 'SAFTCCITT_ALaw_44kHzStereo',
    'DISPID_SOTCSetId', 'DISPID_SpeechRecognizer', 'SVP_20',
    'DISPID_SMSSetData', 'DISPID_SOTDataKey',
    'SPINTERFERENCE_LATENCY_TRUNCATE_END', 'DISPID_SVGetProfiles',
    'DISPID_SVAudioOutputStream', 'SpMMAudioOut',
    'SpNullPhoneConverter', 'DISPID_SpeechObjectTokens',
    'SGRSTTDictation', 'DISPID_SVVolume', 'SPCS_ENABLED',
    'SPPS_RESERVED3', 'ISpNotifySink', 'DISPID_SRSAudioStatus',
    'SP_VISEME_7', 'SPPHRASEREPLACEMENT', 'SPPS_LMA',
    'DISPID_SpeechPhraseBuilder', 'DISPID_SAFGuid', 'DISPID_SRCVoice',
    'DISPID_SPANumberOfElementsInResult', 'eLEXTYPE_RESERVED4',
    'ISpeechRecognizerStatus', 'DISPID_SpeechAudioFormat',
    'SVEViseme', 'SAFTADPCM_8kHzStereo',
    'SpeechRegistryLocalMachineRoot', 'SPVOICESTATUS',
    'SPSTREAMFORMATTYPE', 'ISpPhraseAlt', 'SPEI_SR_RETAINEDAUDIO',
    'DISPID_SVEStreamEnd', 'SpShortcut', 'SRAORetainAudio',
    'SDTDisplayText', 'ISpeechGrammarRuleStateTransitions'
]

