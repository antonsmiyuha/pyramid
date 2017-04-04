class Feedback {

    constructor(formId) {
        this.form = document.getElementById(formId);
        this.otherSubject();
    }

    otherSubject() {
        var subjectOption = document.getElementById('subject');
        var otherSubjectBlock = document.getElementById('other-subject-block');
        var otherSubjectInput = document.getElementById('other-subject');
        subjectOption.addEventListener("change", function (event) {
            if (event.target.value === 'other') {
                otherSubjectBlock.removeAttribute('hidden');
                otherSubjectInput.removeAttribute('disabled');
            } else {
                otherSubjectBlock.setAttribute('hidden', 'true');
                otherSubjectInput.setAttribute('disabled', 'disabled');
            }
        });

    }

}