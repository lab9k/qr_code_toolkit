export const actionTypes = {
  FETCH_ALL_JOBS: 'fetch_all_jobs',
  TRACK_ITEM: 'track_item'
}
export const mutationTypes = {
  UPDATE_JOB_LIST: 'update_job_list'
}
export const getterTypes = {
  JOB_PER_ID: 'job_per_id'
}

export const state = () => ({
  jobs: []
})

export const actions = {
  async [actionTypes.FETCH_ALL_JOBS]({ commit }) {
    const jobs = await this.$axios.$get('/job')
    commit(mutationTypes.UPDATE_JOB_LIST, jobs)
  },
  async [actionTypes.TRACK_ITEM]({ commit }, { job, id: idToTrack }) {
    const item = await this.$axios.$get(`/item/${idToTrack}`)
    item.job = job.id
    const url = `/item/${item.item_id}/`
    await this.$axios.$put(url, item)
  }
}
export const mutations = {
  [mutationTypes.UPDATE_JOB_LIST](state, jobs) {
    state.jobs = [...jobs]
  }
}
export const getters = {
  [getterTypes.JOB_PER_ID]: (state) => (id) =>
    state.jobs.find((job) => job.id === id)
}
