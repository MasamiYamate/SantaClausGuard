const skilUtil = require('../util/skil-util');
const gadgetUtil = require('../util/gadget-tool-util');

const gadgetDirective = require('../directive/gadgetDirectiveFactory.js');

module.exports = {
    santaLocationResponse: santaLocationResponse,
    sessionPersistenceResponse: sessionPersistenceResponse,
    sessionEndResponse: sessionEndResponse,
    gadgetEventHandler: gadgetEventHandler,
    gadgetSantaResponse: gadgetSantaResponse
}

async function santaLocationResponse (handlerInput) {
    let sessionToken = gadgetUtil.sessionToken(handlerInput);
    // 永続化用のディレクティブ
    let persistenceDirective = gadgetDirective.sessionPersistence(sessionToken, null);

    // SessionAttributeからサンタクロースの現在地を取得する
    const attributesManager = handlerInput.attributesManager;
    let sessionAttributes = attributesManager.getSessionAttributes();
    let santaLocationCity = sessionAttributes.santaLocationCity

    if (santaLocationCity) {
        // サンタクロースの現在地がまだ取得できていないとき
        return handlerInput.responseBuilder
            .speak('サンタクロースは、' + santaLocationCity + '付近にいるみたいです！')
            .addDirective(persistenceDirective)
            .getResponse();
    }else{
        // サンタクロースの現在地がまだ取得できていないとき
        return handlerInput.responseBuilder
            .speak('まだ、サンタクロースは日本上空にサンタクロースは来ていないようです！')
            .addDirective(persistenceDirective)
            .getResponse();
    }
}

/**
 * gadgetからサンタクロースの追跡結果を発話させる
 *
 * @param {*} handlerInput
 */
function gadgetSantaResponse (handlerInput) {
    let sessionToken = gadgetUtil.sessionToken(handlerInput);
    // 永続化用のディレクティブ
    let persistenceDirective = gadgetDirective.sessionPersistence(sessionToken, null);

    let payload = gadgetUtil.getPayload(handlerInput);
    let cityName = payload.city_name;

    // ◎時間◎分のセッションを開始しますと読み上げます
    return handlerInput.responseBuilder
    .speak('サンタクロースが日本にいるようです！' + cityName + '付近に今サンタクロースがいるみたいです！')
    .addDirective(persistenceDirective)
    .getResponse();
}

/**
 * ガジェットイベントのHandler
 *
 * @param {*} handlerInput
 * @returns
 */
function gadgetEventHandler (handlerInput) {
    let payload = gadgetUtil.getPayload(handlerInput);
    let cityName = payload.city_name;
    if (cityName) {
        return gadgetSantaResponse(handlerInput);
    }else{
        return sessionPersistenceResponse(handlerInput);
    }
}

/**
 * セッション永続化のBlancResponse用
 *
 * @param {*} handlerInput
 */
function sessionPersistenceResponse (handlerInput) {
    let sessionToken = gadgetUtil.sessionToken(handlerInput);
    // 永続化用のディレクティブ
    let persistenceDirective = gadgetDirective.sessionPersistence(sessionToken, null);
    // ◎時間◎分のセッションを開始しますと読み上げます
    return handlerInput.responseBuilder
        .speak("")
        .addDirective(persistenceDirective)
        .getResponse();
}

/**
 *　セッション終了のResponse
 *
 * @param {*} handlerInput
 * @returns
 */
function sessionEndResponse (handlerInput) {
    return handlerInput.responseBuilder
        .speak("サンタクロースの追跡を終了します")
        .withShouldEndSession(true)
        .getResponse();
}