const gadgetUtil = require('../util/gadget-tool-util');

// ガジェットの名前空間
const nameSpace = 'Custom.SantaGuard';

module.exports = {
    start: start,
    sessionPersistence
}

// セッション永続化のディレクティブを生成する
function sessionPersistence(token, expirationPayload) {
    let names = ['SkillHandler'];
    let nameSpaces = [nameSpace];
    return gadgetUtil.createStartEventHandlerDirective(names, nameSpaces, token, "SEND_AND_TERMINATE", null, expirationPayload);
}